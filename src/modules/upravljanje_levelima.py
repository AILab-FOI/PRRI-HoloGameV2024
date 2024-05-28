player_starting_positions = [ # pocetna pozicija igraca za svaki level (u map editoru se prikazuje):
    [7, 12], # level 0
    [5, 28], # level 1
    [10, 44], # level 2
    [3, 63], # level 3
    [3, 72] # nepostojeci opet peti level
]
level_finish_tile_indexes = [ # indexi tileova sa vratima za zavrsetak levela
    50, 51, 52, 
    66, 67, 68, 
    82, 83, 84,
    211, 212, 213, 
    227, 228, 229, 
    243, 244, 245
]
background_tile_indexes = [ # indexi tileova sa elementima koji nemaju definiraju koliziju (pozadinski elementi)
	69, 70, 71, 
	56, 57, 58, 72, 73, 74, 
	85, 86, 87, 
	102, 103,
    88, 89, 90, 
    118, 119, 120, # zuti stol, no ima problem jer neki leveli koriste sredinu stola za platformu
    48, 49, 64, 65, 80, 81, 96, 97, # ljestve
    104, 11, 30
]
enemies = [ # pocetne pozicije enemyja za svaki level (u editoru se ispisuje koja)
    [Enemy(7, 12), Enemy(20, 13)], # level 0
    [], # level 1
    [Enemy(139, 46), Enemy(74, 46)], # level 2
    [Enemy(64, 62)] # level 3
]
pickups = [ # pocetna pozicija pick up pusaka za svaki level (u editoru se ispisuje koja)
    [PromjenaPuska(10, 4)], # level 0
    [], # level 1
    [PromjenaPuska(138, 39, 0), PromjenaPuska(74, 39)], # level 2
    [] # level 3
]

# sljedece varijable NE MIJENJATI:
LEVEL_HEIGHT = 17

def ZapocniLevel(level): # poziva se u menu.py kada se odabere opcija da se uđe u level
    tile_size = 8
    starting_pos = player_starting_positions[level]
    player.x = starting_pos[0]*tile_size
    player.y = (starting_pos[1] - LEVEL_HEIGHT*level)*tile_size
    pogled.x = max(0, player.x - (pogled.w - player.width)/2)
    player.hsp = 0
    player.vsp = 0

def IgrajLevel():
    cls(0)
    map(0, level*LEVEL_HEIGHT, 240, 18, -int(pogled.x), -int(pogled.y), 0)
    HUD()
    tile_size = 8
    levelEnemies = enemies[level]
    for enemy in levelEnemies:
        while (enemy.y > LEVEL_HEIGHT*tile_size):
            enemy.y -= LEVEL_HEIGHT*tile_size
    collidables = DefinirajKolizije([player, levelEnemies, metci, projectiles], level, LEVEL_HEIGHT)
    for enemy in levelEnemies:
        enemy.movement(collidables)
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
    levelPickups = pickups[level]
    for pickup in levelPickups:
        while (pickup.y > LEVEL_HEIGHT*tile_size):
            pickup.y -= LEVEL_HEIGHT*tile_size
        pickup.PickUp()
    ProvjeravajJeLiIgracKodVrata()

def HUD():
    rect(0, 0, 240, 8, 0)
    print("Level: 1", 1, 1, 12, True, 1, False)
    spr(364, 58, 0, 6, 1, 0, 0, 1, 1)
    rect(70, 1, 100, 5, 6)
    if Puska.tp == 0:
       spr(360, 230, 1, 6, 1, 0, 0, 1, 1)
    else:	
       spr(376, 230, 1, 6, 1, 0, 0, 1, 1)
    print("Ammo: 5", 180, 1, 12, True, 1, False)

def ProvjeravajJeLiIgracKodVrata(): # sluzi za kraj levela
    tile_size = 8
    kojiTile = mget(round(player.x/tile_size), round(player.y/tile_size) + level*LEVEL_HEIGHT)
    if kojiTile in level_finish_tile_indexes:
        ZavrsiLevel()

def ZavrsiLevel():
    global level
    level = level + 1
    ZapocniLevel(level)