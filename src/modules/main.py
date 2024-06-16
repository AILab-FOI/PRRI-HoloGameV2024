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
     print("Keys (AD) for moving left and right", 0, 16)
     print("Keys (WS) for moving up and down by laders", 0, 24)
     print("Key (B) for jump, key (E) for weapon change", 0, 32)
     print("Key (F) for shooting. Be aware of lava nad spikes!!!", 0, 40)
     print("Touching the enemy also decreases health!!!", 0, 48)
 elif state=='menu':
   menu.Menu()
 elif state=='over':
   menu.Over()
 elif state=='win':
   menu.PrikaziZaslonPobjede()

def Final():
	cls(13) 
