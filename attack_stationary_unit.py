# from right to middel attack
# 13 stationary at least
mid_attack_from_right = [[10, 13], [11, 13], [12, 13], [13, 13], [14, 13], [15, 13], [16, 13], [17, 13], [18, 13], [19, 13], [20, 13], [21, 12], [22, 11]]

def middle_attack(self,game_state):#Enemy points
    # check which layer to attack
    attack_start = [22, 8]
    mid_destructors_points_1 = [[12, 13], [17, 13], [21, 12]]
    mid_encryptors_points_1 = [[10, 13], [11, 13], [13, 13], [14, 13], [15, 13], [16, 13], [18, 13], [19, 13], [20, 13], [22, 11]]# check if we can build at once
    # check if resource enough
    for loc in mid_destructors_points_1:
        game_state.attempt_spawn(DESTRUCTOR, loc, 1)
    for loc in mid_encryptors_points_1:
        game_state.attempt_spawn(ENCRYPTOR, loc, 1)
    # place unit
    n = random.randint(1,5)
    game_state.attempt_spawn(EMP, attack_start, n) # at least 5
