prev_key_space = False
prev_key_switch = False

def update_keys():
    global key_space, key_left, key_right, key_up, key_down, key_shoot, key_switch
    global prev_key_space, prev_key_switch

    current_key_space = key(48)
    current_key_switch = key(5)

    key_space = current_key_space and not prev_key_space
    key_switch = current_key_switch and not prev_key_switch

    key_left = key(1)
    key_right = key(4)
    key_up = key(23)
    key_down = key(19)
    key_shoot = key(6)

    prev_key_space = current_key_space
    prev_key_switch = current_key_switch