player_starting_positions = [ # pocetna pozicija igraca za svaki level (u map editoru se prikazuje):
    [7, 12], # level 0
    [0, 30], # level 1
    [10, 44], # level 2
    [3, 63] # level 3
]
level_finish_tile_indexes = [ # indexi tileova sa vratima za zavrsetak levela
    50, 51, 52, 
    66, 67, 68, 
    82, 83, 84
]
LEVEL_HEIGHT = 17

def ZapocniLevel(level): # poziva se u menu.py kada se odabere opcija da se uđe u level
    tile_size = 8
    starting_pos = player_starting_positions[level]
    player.x = starting_pos[0]*tile_size
    player.y = (starting_pos[1] - LEVEL_HEIGHT*level)*tile_size
    Pogled.x = player.x - (pogled.w - player.width)/2

def IgrajLevel():
    cls(0)
    map(0, level*LEVEL_HEIGHT, 240, 18, -int(pogled.x), -int(pogled.y), 0)

    collidables = DefinirajKolizije([player, enemy, metci, projectiles], level, LEVEL_HEIGHT)
    #enemy.movement(enemy, collidables)
    for projektil in projectiles:
        projektil.movement()
        Projectile.MetakCheck(projektil, collidables)
    Puska.Pucanje()
    player.PlayerKontroler(player, collidables)
    pogled.pratiIgraca()
    for metak in metci:
        Metak.MetakCheck(metak, collidables)
    for metak in projectiles:
        Projectile.MetakCheck(metak, collidables)
    PromjenaPuska.PickUp(PromjenaPuska)
    ProvjeravajJeLiIgracKodVrata()

def ProvjeravajJeLiIgracKodVrata(): # sluzi za kraj levela
    tile_size = 8
    kojiTile = mget(round(player.x/tile_size), round(player.y/tile_size) + level*LEVEL_HEIGHT)
    print(level, 16, 16)
    if kojiTile in level_finish_tile_indexes:
        print("LOL!!!", 16, 32)
        ZavrsiLevel()

def ZavrsiLevel():
    global level
    level = level + 1
    ZapocniLevel(level)