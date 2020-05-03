# -*- coding: utf-8 -*-
"""
    ----
 -----------
- Level 314 -
 -----------
    ----

@author: Alexander Williams
date: Sun May  3 10:16:03 2020

"""

import numpy as np
import matplotlib.pyplot as plt

def map_orientation(cur_orientation, cur_count):
    """ . . . . . x
        . . . . . x
        . . . . . x
        . . . . . x
        . . . . . x
        . . . . . x
    """
    right_edge = 34905131040
    """ . . . . . .
        . . . . . .
        . . . . . .
        . . . . . .
        . . . . . .
        x x x x x x
    """
    bottom_edge = 67645734912
    
    """ we will check if each position of the game peice is valid
        by investigating if it touches the right edge or the bottom edge
        using a logica AND (&) operation. The & will be 0 if there is
        no overlap and <> 0 if there is
        
        Pass in peices positioned in the upper left corner so that this
        check can walk right and down to checkk all conditions
    """
    room_to_move_right = True
    room_to_move_down = True
    safe_down = True
    
    while safe_down:
        room_to_move_right = True
        safe_right = True
        row_start = cur_orientation
        while safe_right:
            peice_orientation_list[cur_count] = cur_orientation
            cur_count += 1
            """ moving piece right 1 bit is the same as multiplying by 2^1
                . x . . . .
                x x x . . .  = 450
                
                . . x . . .
                . x x x . .  = 900
            """
            if room_to_move_right:
                cur_orientation = cur_orientation << 1
                room_to_move_right = ((cur_orientation & right_edge) == 0)
            else:
                safe_right = False
    
        """ moving down is the same as shifting right 6 times or multiplying by 2^6, aka 64
            . x . . . .
            x x x . . .  = 450
            
            . x . . . .
            x x x . . .  = 28,800
        """
        if room_to_move_down:
            cur_orientation = row_start << 6
            room_to_move_down = ((cur_orientation & bottom_edge) == 0)
        else:
            safe_down = False
    
    return cur_count


def SolveGame(game_id, max_wins = 10):
    # game_id, number of wins
    result_hdr = [game_id, 0]
    # game_id (peg_bits), peice bits
    result_detail = [[0] * (total_peices + 1)] * 10
    single_result = [0] * (total_peices + 1)
    
    peice_counter = [0] * total_peices
    full_board = (2**36) - 1
    board_now = [0] * total_peices
    single_result[0]=game_id
    
    try_count = 0
    # initialize board
    # peice 1
    for peice_counter[0] in range(po_start[0], po_end[0]):
        try_count += 1
        if ((peice_orientation_list[peice_counter[0]] & game_id) == 0):
            board_now[0] = game_id | peice_orientation_list[peice_counter[0]]
            single_result[1]=peice_orientation_list[peice_counter[0]]
            # peice 2
            for peice_counter[1] in range(po_start[1], po_end[1]):
                try_count += 1
                if ((peice_orientation_list[peice_counter[1]] & board_now[0]) == 0):
                    board_now[1] = board_now[0] | peice_orientation_list[peice_counter[1]]
                    single_result[2]=peice_orientation_list[peice_counter[1]]
                    # peice 3
                    for peice_counter[2] in range(po_start[2], po_end[2]):
                        try_count += 1
                        if ((peice_orientation_list[peice_counter[2]] & board_now[1]) == 0):
                            board_now[2] = board_now[1] | peice_orientation_list[peice_counter[2]]
                            single_result[3]=peice_orientation_list[peice_counter[2]]
                            # peice 4
                            for peice_counter[3] in range(po_start[3], po_end[3]):
                                try_count += 1
                                if ((peice_orientation_list[peice_counter[3]] & board_now[2]) == 0):
                                    board_now[3] = board_now[2] | peice_orientation_list[peice_counter[3]]
                                    single_result[4]=peice_orientation_list[peice_counter[3]]
                                    # peice 5
                                    for peice_counter[4] in range(po_start[4], po_end[4]):
                                        try_count += 1
                                        if ((peice_orientation_list[peice_counter[4]] & board_now[3]) == 0):
                                            board_now[4] = board_now[3] | peice_orientation_list[peice_counter[4]]
                                            single_result[5]=peice_orientation_list[peice_counter[4]]
                                            # peice 6
                                            for peice_counter[5] in range(po_start[5], po_end[5]):
                                                try_count += 1
                                                if ((peice_orientation_list[peice_counter[5]] & board_now[4]) == 0):
                                                    board_now[5] = board_now[4] | peice_orientation_list[peice_counter[5]]
                                                    single_result[6]=peice_orientation_list[peice_counter[5]]
                                                    # peice 7
                                                    for peice_counter[6] in range(po_start[6], po_end[6]):
                                                        try_count += 1
                                                        if ((peice_orientation_list[peice_counter[6]] & board_now[5]) == 0):
                                                            board_now[6] = board_now[5] | peice_orientation_list[peice_counter[6]]
                                                            single_result[7]=peice_orientation_list[peice_counter[6]]
                                                            # peice 8
                                                            for peice_counter[7] in range(po_start[7], po_end[7]):
                                                                try_count += 1
                                                                if ((peice_orientation_list[peice_counter[7]] & board_now[6]) == 0):
                                                                    try_count += 1
                                                                    board_now[7] = board_now[6] | peice_orientation_list[peice_counter[7]]
                                                                    single_result[8]=peice_orientation_list[peice_counter[7]]
                                                                    # peice 9 automatically fits
                                                                    # find it's location and save this winner
                                                                    single_result[9] = board_now[7] ^ full_board
                                                                    result_detail[result_hdr[1]]=single_result.copy()
                                                                    result_hdr[1] += 1
                                                                    
                                                                    if result_hdr[1] == max_wins:
                                                                        break
                                                            if result_hdr[1] == max_wins:
                                                                break
                                                    if result_hdr[1] == max_wins:
                                                        break
                                            if result_hdr[1] == max_wins:
                                                break
                                    if result_hdr[1] == max_wins:
                                        break
                            if result_hdr[1] == max_wins:
                                break
                    if result_hdr[1] == max_wins:
                        break
            if result_hdr[1] == max_wins:
                break
        
    print('Number of tries: {:,}'.format(try_count))
    return result_hdr, result_detail

def StringToId(peg_positions):
    """ input a list of strings representing peg positions
        returns the game bitfield as integer number
    """
    my_string = [''] * 36
    cur_pos = 0
    cur_bitfield = 0
    
    for row in ['A', 'B', 'C', 'D', 'E', 'F']:
        for col in ['1', '2', '3', '4', '5', '6']:
            my_string[cur_pos] = row + col
            cur_pos += 1
    
    for this_peg in peg_positions:
        cur_bitfield = cur_bitfield | (2 ** my_string.index(this_peg))
        
    return cur_bitfield
    
def IdToString(peg_bitfield):
    """ input peg position bitfield
        returns the peg positions as a string
    """
    my_string = [''] * 36
    result_string = [''] * 7
    cur_pos = 0
    
    for row in ['A', 'B', 'C', 'D', 'E', 'F']:
        for col in ['1', '2', '3', '4', '5', '6']:
            my_string[cur_pos] = row + col
            cur_pos += 1

    cur_pos = 0
    for row in range(6):
        for col in range(6):
            if (2**(row * 6 + col) & peg_bitfield) != 0:
                result_string[cur_pos] = my_string[row * 6 + col]
                cur_pos += 1
    
        
    return result_string
    
def PlotGame(result_detail):
    """ plot the game
        result_detail = [game_id (peg positions), game_peices]
    """
    set_bits = 0
    board_array = np.zeros((6,6))
    # pegs
    board_array = board_array + (((board_sieve & result_detail[0]) == board_sieve) * peg_cmap_value)
    set_bits = set_bits | result_detail[0]
    # game peices
    for i in range(total_peices):
        board_array = board_array + (((board_sieve & result_detail[i+1]) == board_sieve) * peice_cmap_value[i])
        set_bits = set_bits | result_detail[i+1]
    # empty spots
    unset_bits = set_bits ^ ((2^36) - 1)
    board_array = board_array + (((board_sieve ^ unset_bits) == board_sieve) * empty_cmap_value)

    # plot board    
    plt.matshow(board_array, cmap=plt.cm.tab20)
    
    # show labels
    row_labels = ['A', 'B', 'C', 'D', 'E', 'F']
    col_labels = range(1, 7)
    plt.xticks(range(6), col_labels)
    plt.yticks(range(6), row_labels)

    # mark the pegs
    for row in range(6):
        for col in range(6):
            if (2**(row * 6 + col) & result_detail[0]) != 0:
                plt.text(col, row, 'O', horizontalalignment='center',
                verticalalignment='center', fontweight = 'bold', fontsize = 'xx-large')
            
    plt.show()


# start main program logic
    
# initialize game peices meta variables
total_peices = 9 
total_orientations = 625
peice_orientation_list = [0] * total_orientations
po_start = [0] * total_peices
po_end = [0] * total_peices
peice_name = ['red', 'cyan', 'grey', 'yellow', 'green', 'orange', 'purple', 'brown', 'blue']

# set up color map for plotting results
cmap_map = np.linspace(0,1,20)
peice_cmap_value = np.zeros(total_peices)
peice_cmap_value[0] = cmap_map[6]
peice_cmap_value[1] = cmap_map[19]
peice_cmap_value[2] = cmap_map[14]
peice_cmap_value[3] = cmap_map[17]
peice_cmap_value[4] = cmap_map[4]
peice_cmap_value[5] = cmap_map[2]
peice_cmap_value[6] = cmap_map[8]
peice_cmap_value[7] = cmap_map[10]
peice_cmap_value[8] = cmap_map[0]
peg_cmap_value = cmap_map[3]
empty_cmap_value = cmap_map[15]
board_sieve = np.array([2**i for i in range(36)]).reshape((6,6))


# set up game peice orientations
cur_orientation_count = 0
""" red peice (1) orientation (1)
    1.1
"""
po_start[0] = cur_orientation_count
this_peice = 387
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 1.2
this_peice = 4290
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 1.3
this_peice = 198
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 1.4
this_peice = 8385
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
po_end[0] = cur_orientation_count

""" cyan peice (2) orientation (1)
    2.1
"""
po_start[1] = cur_orientation_count
this_peice = 452
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 2.2
this_peice = 8323
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 2.3
this_peice = 71
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 2.4
this_peice = 12353
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 2.5
this_peice = 263
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 2.6
this_peice = 4163
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 2.7
this_peice = 449
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 2.8
this_peice = 12418
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
po_end[1] = cur_orientation_count

""" grey peice (3) orientation (1)
    3.1
"""
po_start[2] = cur_orientation_count
this_peice = 15
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 3.2
this_peice = 266305
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
po_end[2] = cur_orientation_count

""" yellow peice (4) orientation (1)
    4.1
"""
po_start[3] = cur_orientation_count
this_peice = 450
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 4.2
this_peice = 4289
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 4.3
this_peice = 135
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 4.4
this_peice = 8386
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
po_end[3] = cur_orientation_count


""" green peice (5) orientation (1)
    5.1
"""
po_start[4] = cur_orientation_count
this_peice = 195
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
po_end[4] = cur_orientation_count

""" orange peice (6) orientation (1)
    6.1
"""
po_start[5] = cur_orientation_count
this_peice = 7
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 6.2
this_peice = 4161
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
po_end[5] = cur_orientation_count

""" purple peice (7) orientation (1)
    7.1
"""
po_start[6] = cur_orientation_count
this_peice =  193 
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 7.2
this_peice = 194
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 7.3
this_peice =  131
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 7.4
this_peice = 67
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
po_end[6] = cur_orientation_count

""" brown peice (8) orientation (1)
    8.1
"""
po_start[7] = cur_orientation_count
this_peice = 3
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
# 8.2
this_peice = 65
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
po_end[7] = cur_orientation_count

""" blue peice (9) orientation (1)
    9.1
"""
po_start[8] = cur_orientation_count
this_peice = 1
cur_orientation_count = map_orientation(this_peice, cur_orientation_count)
po_end[8] = cur_orientation_count

# print(cur_orientation_count)
# print(peice_orientation_list)
# print(po_start, po_end)

game_id = StringToId(['A3', 'B2', 'B4', 'C2', 'C3', 'C5', 'C6'])
(res_hdr, res_detail) = SolveGame(game_id, 10) 
print(res_hdr, res_detail)

for i in range(res_hdr[1]):
    PlotGame(res_detail[i])
