# title:   HoloGameV
# author:  AILab-FOI
# desc:    short description
# site:    https://ai.foi.hr
# license: GPLv3
# version: 0.1
# script:  python


state='menu' #varijabla za game state

level = 0 # koji level je ucitan (od 0 pa na dalje)

def TIC():
 
 ShowHealth()
 
 Final()
 global state
 if state=='game':
   IgrajLevel()
   ShowHealth()
 elif state=='menu':
   menu.Menu()
   
 
   
 
 

def ShowHealth():
  for i in range(player.health):
    rect(10 * i, 10, 3, 3, 10)

def Final():
	cls(13) 