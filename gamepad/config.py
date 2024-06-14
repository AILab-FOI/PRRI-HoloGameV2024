#!/usr/bin/env python3



abe = {
    "title": "Abe's Amazing Adventure",
    "players": 1,
    "executable": "/usr/games/abe",
    'toggles': ['UP', 'DOWN', 'LEFT', 'RIGHT'],
    'taps': ['SELECT', 'START', 'A', 'B'],
    "description": """A scrolling, platform-jumping, key-collecting, ancient pyramid exploring game, vaguely in the style of similar games for the Commodore+4. The game is intended to show young people (I'm writing it for my son's birthday) all the cool games they missed.""",
    "website": "abe.sourceforge.net",
    "developer": "Gabor Torok",
    "controls": [
        {
            'UP': 'up',
            'DOWN': 'down',
            'LEFT': 'left',
            'RIGHT': 'right',
            'SELECT': 'esc',
            'START': 'enter',
            'A': 'space',
            'B': 'enter'
        }
    ]
}

hologamev = {
    "title": "HoloGame V",
    "players": 1,
    "executable": "\"C:\\Users\\dinob\\Desktop\\tic80 2.0.exe\"",
    'toggles': ['UP', 'DOWN', 'LEFT', 'RIGHT'],
    'taps': ['SELECT', 'START', 'A', 'B'],
    "description": """A TIC-80 game.""",
    "website": "example.com",
    "developer": "Your Name",
    "controls": [
        {
            'UP': 'W',
            'DOWN': 'S',
            'LEFT': 'A',
            'RIGHT': 'D',
            'SELECT': 'E',
            'START': 'space',
            'A': 'F',
            'B': 'space'
        }
    ]
}

GAMES = { "abe": abe, "hologamev": hologamev }
