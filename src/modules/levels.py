player_starting_positions = [ # pocetna pozicija igraca za svaki level (u map editoru se prikazuje):
  [7, 12], # level 0
  [0, 30], # level 1
  [10, 44], # level 2
  [3, 63] # level 3
]
LEVEL_HEIGHT = 17

def ZapocniLevel(level): # poziva se u menu.py kada se odabere opcija da se uđe u level
  tile_size = 8
  player.ProvjeriKolizije(player, 0, 0)
  starting_pos = player_starting_positions[level]
  player.x = starting_pos[0]*tile_size
  player.y = (starting_pos[1] - LEVEL_HEIGHT*level)*tile_size