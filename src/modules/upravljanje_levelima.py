player_starting_positions = [ # pocetna pozicija igraca za svaki level (u map editoru se prikazuje):
    [2, 12], # level 0
    [5, 28], # level 1
    [9, 44], # level 2
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
    104, 11, 30,
    59, 231, 247,
    219, 220, 221, 222, 223, # oni "ormarici"
    235, 236, 237, 238, 239,
    251, 252, 253, 254, 255,
    133, 134, # torta
]
enemies = [ # pocetne pozicije enemyja za svaki level (u editoru se ispisuje koja)
    [], # level 0
    [Enemy(60, 30),Enemy(79, 30), Enemy(182, 35)], # level 1
    [Enemy2(139, 46), Enemy2(79, 46), Enemy2(58, 46), Enemy2(127, 46), Enemy2(184, 46), Enemy2(174, 46)], # level 2
    [Enemy3(64, 62), Enemy3(154, 56), Enemy3(167, 61), Enemy3(206, 65), Enemy3(197, 65)] # level 3
]
pickups = [ # pocetna pozicija pick up pusaka za svaki level (u editoru se ispisuje koja)
    [], # level 0
    [PromjenaPuska(130, 22, 1)], # level 1
    [PromjenaPuska(168, 40, 2)], # level 2
    [] # level 3
]
lava = [ # tile lave
    59
]
spikes = [ # tileovi spikeova
    231, 247
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
        Metak.MetakCheck(metak, collidables, enemies)
    for metak in projectiles:
        Projectile.MetakCheck(metak, collidables)
    levelPickups = pickups[level]
    for pickup in levelPickups:
        while (pickup.y > LEVEL_HEIGHT*tile_size):
            pickup.y -= LEVEL_HEIGHT*tile_size
        pickup.PickUp()
    ProvjeravajJeLiIgracKodVrata()
    ProvjeravajJeLiIgracULavi()
    ProvjeravajJeLiIgracNaSiljku()

def ProvjeravajJeLiIgracKodVrata(): # sluzi za kraj levela
    tile_size = 8
    kojiTile = mget(round(player.x/tile_size), round(player.y/tile_size) + level*LEVEL_HEIGHT)
    if kojiTile in level_finish_tile_indexes:
        sfx(6, "C-4", 15, 0, 2, 1)
        ZavrsiLevel()
        
def ProvjeravajJeLiIgracULavi():
    tile_size = 8
    kojiTile = mget(round(player.x/tile_size), round(player.y/tile_size) + level*LEVEL_HEIGHT)
    if kojiTile in lava:
        sfx(8, "C-4", 15, 0, 2, 1)
        player.Pogoden(player, 1)
    
def ProvjeravajJeLiIgracNaSiljku():
    tile_size = 8
    kojiTile = mget(round(player.x/tile_size), round(player.y/tile_size) + 1 + level*LEVEL_HEIGHT)
    if kojiTile in spikes:
        sfx(8, "C-4", 15, 0, 2, 1)
        player.Pogoden(player, 1)

def ZavrsiLevel():
    global level
    level = level + 1
    if level <=3:
        ZapocniLevel(level)
    else:
        global state
        state = 'win'

def HUD():
    rect(0, 0, 240, 8, 0)
    print("Level:" + str(level), 1, 1, 12, True, 1, False)
    # Prikaz zivota
    spr(364, 50, 0, 6, 1, 0, 0, 1, 1)
    rect(60, 1, player.health*10, 5, 6)
    if player.health > 0:
        rect(60+player.health*10, 1, 50-player.health*10, 5, 3)
        print(str(player.health) + "HP", 120, 1, 12, True, 1, False)
    else: 
        print("0HP", 120, 1, 12, True, 1, False)
    # Prikaz puske i metaka
    spr(Puska.svespr[Puska.p[Puska.tp]], 150, 0, 6, 1, 0, 0, 1, 1)
