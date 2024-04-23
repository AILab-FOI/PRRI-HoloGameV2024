m_ind=0

def Menu():
    global m_ind
    cls(0)
    rectb(0,0,240,136,12)
    print('NEON ESCAPE', 30, 20, 4, False, 2, False)

# Opcije menija
    rect(1,48+10*m_ind,238,10,2)
    print('Play', 40, 50, 4, False, 1, False)
    print('Quit', 40, 60, 4, False, 1, False)

#  Šetanje po opcijama na meniju
    if btnp(1) and 48+10*m_ind<50: #ako se budu dodavale još koje opcije, promijeniti uvijet
        m_ind += 1
    elif btnp(0) and 48+10*m_ind>=50:
        m_ind += -1
