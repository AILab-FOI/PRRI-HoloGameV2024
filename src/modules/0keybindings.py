prev_key_space = False
prev_key_switch = False

def update_keys():
    global key_space, key_left, key_right, key_up, key_down, key_shoot, key_switch
    global prev_key_space, prev_key_switch

    current_key_space = key(48) # 'SPACE' ili 'START' ili 'B' na gamepadu (prirodno skakati na B, a birati na 'START')
    current_key_switch = key(5) # 'E' ili 'SELECT' na gamepadu

    key_space = current_key_space and not prev_key_space
    key_switch = current_key_switch and not prev_key_switch

    key_left = key(1) # 'A' ili lijevo na gamepadu
    key_right = key(4) # 'D' ili desno na gamepadu
    key_up = key(23) # 'W' ili gore na gamepadu
    key_down = key(19) # 'S' ili dolje na gamepadu
    key_shoot = key(6) # 'F' ili 'A' na gamepadu

    prev_key_space = current_key_space
    prev_key_switch = current_key_switch