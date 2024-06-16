

class menu:
    m_ind=0

    def Menu():
        global state
        cls(0)
        menu.AnimateFrame()
        menu.AnimateTitle()

        # Opcije menija
        rect(1,48+10*menu.m_ind,238,10,2)
        print('Play', 100, 50, 4, False, 1, False)
        print('Quit', 100, 60, 4, False, 1, False)

        #  Šetanje po opcijama na meniju
        if key_down and 48+10*menu.m_ind<50: #ako se budu dodavale još koje opcije, promijeniti uvijet
            menu.m_ind += 1
        elif key_up and 48+10*menu.m_ind>=50:
            menu.m_ind += -1

        # Odabir 
        if key_space and menu.m_ind==0:
            state = 'game'
            ZapocniLevel(level)
        elif key_space and menu.m_ind==1:
            exit()

    def AnimateTitle():
        if(time()%500>250):
            print('NEON ESCAPE', 57, 20, 6, False, 2, False)
        elif(time()%500>150):
            print('NEON ESCAPE', 57, 20, 2, False, 2, False)
        elif(time()%500>350):
            print('NEON ESCAPE', 57, 20, 3, False, 2, False)
        elif(time()%500>550):
            print('NEON ESCAPE', 57, 20, 10, False, 2, False)

    def AnimateFrame():
        if(time()%500>250):
            rectb(0,0,240,136,6)
        elif(time()%500>150):
            rectb(0,0,240,136,2)
        elif(time()%500>350):
            rectb(0,0,240,136,3)
        elif(time()%500>550):
            rectb(0,0,240,136,10)

    def AnimateWinTitle():
        if(time()%500>250):
            print('YOU WON!', 57, 20, 6, False, 2, False)
        elif(time()%500>150):
            print('YOU WON!', 57, 20, 2, False, 2, False)
        elif(time()%500>350):
            print('YOU WON!', 57, 20, 3, False, 2, False)
        elif(time()%500>550):
            print('YOU WON!', 57, 20, 10, False, 2, False)
            
    def Over():

        print('GAME OVER', 100, 50, 4, False, 1, False)
        print('START (space) za reset', 64, 70, 4, False, 1, False)
        
        if key_space:
            reset()

    def PrikaziZaslonPobjede():
        global state
        cls(0)
        menu.AnimateFrame()
        menu.AnimateWinTitle()

        rect(1,48+10*menu.m_ind,238,10,2)
