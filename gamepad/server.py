#!/usr/bin/env python3

import flask
from flask import Flask, render_template, send_from_directory, request, abort
from flask_socketio import SocketIO, emit
import json
import subprocess
import threading

from config import GAMES
import sys
sys.path.append("../src/modules")
from controller import pomakni, player

GAME = GAMES['hologamev']  # change this when multiple games are available

ADDR_OUT = '0.0.0.0'
PORT = 5000

app = Flask(__name__)
app.config['SECRET_KEY'] = 'šekret'
socketio = SocketIO(app, cors_allowed_origins="*")

PLAYERS = 0
GAME_STARTED = False

# A set to keep track of connected clients
connected_clients = set()
player_lock = threading.Lock()

game_player = player()
key_states = {'left': False, 'right': False, 'jump': False, 'jetpack': False}

def popen_and_call(on_exit, *popen_args):
    """
    Runs the given args in a subprocess.Popen, and then calls the function
    on_exit when the subprocess completes.
    on_exit is a callable object, and popen_args is a list/tuple of args that 
    would give to subprocess.Popen.
    
    Adapted from: http://stackoverflow.com/questions/2581817/python-subprocess-callback-when-cmd-exits
    """

    def run_in_thread(on_exit, *popen_args):
        proc = subprocess.Popen(*popen_args)
        proc.wait()
        on_exit()
        return

    thread = threading.Thread(target=run_in_thread, args=(on_exit, *popen_args))
    thread.start()
    # returns immediately after the thread starts
    return thread

def run_tic_80(game_script):
    subprocess.run(["tic-80", "-code", f"load('{game_script}')", "-code", "run()"])


@socketio.on('connect')
def connect():
    print('Client connected:', request.sid)
    connected_clients.add(request.sid)
    global PLAYERS
    PLAYERS += 1
    print("total players: ", PLAYERS)

    if(PLAYERS == 1):
        print("running tic-80 hologamev.py")
        run_tic_80("hologamev.py")

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected:', request.sid)
    connected_clients.remove(request.sid)
    global PLAYERS
    PLAYERS -= 1
    print("total players: ", PLAYERS)

@socketio.on('ctrl')
def handle_message(message):
    print('ctrl', message)
    global PLAYERS, GAME_STARTED, GAMES
    if not GAME_STARTED:
        print('Game aborted or not started! Player', PLAYERS)
        emit('error', {"message": "Game hasn't started or stopped running!"}, broadcast=True)
        return

    try:
        msg = json.loads(message['data'])
    except Exception as e:
        print("Error while loading message:", message)
        emit('error', {"message": "Your browser sent an unparsable message."}, broadcast=True)
        return

    cmd = msg["cmd"]
    context = msg["context"]
    game = msg["game"]

    if PLAYERS > GAMES[game]["players"]:
        print("Too many players! Player", PLAYERS)
        emit('error', {"message": "Too many players already connected for this game."}, broadcast=True)
        return

    # TODO: add controls for other players
    try:
        toggles = GAMES[game]["controls"][PLAYERS - 1]
    except Exception as e:
        print("Error, unknown game! Player", PLAYERS)
        emit('error', {"message": "Error! Unknown game!"}, broadcast=True)
        return
    
    if cmd in GAMES[game]['taps']:
        if context == "start":
            pomakni(game_player.hsp, -game_player.maxBrzina, game_player.akceleracija)
            # Adjust control as needed for your game

    if cmd in GAMES[game]['toggles']:
        if context == "start":
            pomakni(game_player.hsp, game_player.maxBrzina, game_player.akceleracija)
            # Adjust control as needed for your game

    print('Player', PLAYERS, 'Got', cmd, context)


# Route for serving the controller
@app.route('/')
def ctrl():
    global GAME_STARTED
    def game_exit_callback():
        GAME_STARTED = False
        print('Game finished! Asking clients to stop.')
        socketio.server.emit('stop', broadcast=True)  # TODO: Not working for some reason!
        print('Done!')

    popen_and_call(lambda: game_exit_callback(), GAME['executable'])
    GAME_STARTED = True  
    return render_template('ctrl.html', game='hologamev')


# Route for serving the start button
@app.route('/start')
def start():
    return render_template('index.html')

# Routes for serving static files
@app.route('/images/<path:path>')
def serve_images(path):
    return send_from_directory('images', path)

@app.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('js', path)

if __name__ == '__main__':
    print('Starting server ...')
    socketio.run(app, host='0.0.0.0', port=5000)
