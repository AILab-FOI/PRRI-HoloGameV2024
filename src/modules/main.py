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
 Final()

 global state
 if state=='game':
   IgrajLevel()
   if level == 0:
     print("WASD za micanje, F za pucanje", 0, 16)
     print("E za promjenu oruzja", 0, 22)
 elif state=='menu':
   menu.Menu()
 elif state=='over':
   menu.Over()

def Final():
	cls(13) 
