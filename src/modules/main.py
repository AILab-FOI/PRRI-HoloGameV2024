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
 update_keys()

 Final()

 global state
 if state=='game':
   IgrajLevel()
   if level == 0:
     print("Strjelice (WASD) za micanje, A (F) za pucanje", 0, 16)
     print("SELECT (E) za promjenu oruzja", 0, 22)
 elif state=='menu':
   menu.Menu()
 elif state=='over':
   menu.Over()
 elif state=='win':
   menu.PrikaziZaslonPobjede()

def Final():
	cls(13) 
