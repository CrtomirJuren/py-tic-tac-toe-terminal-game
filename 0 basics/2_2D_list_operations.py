# # game board   
board = list(range(9))

# # board[0] = 'X'
# # board[4] = 'X'
# # board[8] = 'X'
# # board[7] = 'O'

# print(board)

# # Funkcija za list elemente
# # list_subset = list[start_index:stop_index:step]

# # --- VRSTICE ---

# # vrstica je sestavljena, iz 3 zaporednih elementov
# # 1,2,3 | 4,5,6 | 7,8,9
# row_1 = board[0:3] # 1,2,3
# row_2 = board[3:6] # 4,5,6
# row_3 = board[6:9] # 7,8,9

# print('\n',row_1,'\n',row_2,'\n',row_3)

# print('row_1:', row_1)
# print('row_2:', row_2)
# print('row_3:', row_3)

# # --- STOLPCI ---
# # stolpec je vsak element za tri indexe večji
# column_1 = board[0:9:3]
# column_2 = board[1:9:3]
# column_3 = board[2:9:3]

# print('column_1:', column_1)
# print('column_2:', column_2)
# print('column_3:', column_3)

# # --- DIAGONALE ---
# diagonal_1 = board[0:9:4] # 0 | 4 | 8

# # MIRROR BOARD # 2 | 4 | 6
# diagonal_1 = [board[0],board[4],board[8]] # 0 | 4 | 8
# diagonal_2 = [board[2],board[4],board[6]] # 2 | 4 | 6

# d_1_win = (diagonal_1.count(player) == 3)
# d_2_win = (diagonal_2.count(player) == 3)

# win = (d_1_win or d_2_win)

# print('board_mirrored:', board_mirrored)
# print('diagonal_1:', diagonal_1)
# print('diagonal_2:', diagonal_2)

# create board with 1st row full

# create board with 1st column full

# create board with 1st diagonals full

def check_rows(board, player): 
    """ 3 rows check """

    row_1 = board[0:3] # 1,2,3
    row_2 = board[3:6] # 4,5,6
    row_3 = board[6:9] # 7,8,9

    r_1_win = (row_1.count(player) == 3)
    r_2_win = (row_2.count(player) == 3)
    r_3_win = (row_3.count(player) == 3)

    win = (r_1_win or r_2_win or r_3_win)

    return win

def check_columns(board,player): 
    """ 3 columns check """
    # stolpec je vsak element za tri indexe večji
    column_1 = board[0:9:3]
    column_2 = board[1:9:3]
    column_3 = board[2:9:3]
    
    # win if 3 in a column
    c_1_win = (column_1.count(player) == 3)
    c_2_win = (column_2.count(player) == 3)
    c_3_win = (column_3.count(player) == 3)

    win = (c_1_win or c_2_win or c_3_win)

    return win

def check_diagonals(board, player):
    """ 2 diagonals check """
    diagonal_1 = [board[0],board[4],board[8]] # 0 | 4 | 8
    diagonal_2 = [board[2],board[4],board[6]] # 2 | 4 | 6

    d_1_win = (diagonal_1.count(player) == 3)
    d_2_win = (diagonal_2.count(player) == 3)

    win = (d_1_win or d_2_win)

    return win

print(check_rows(board_2,'X'))
print(check_columns(board_7,'X'))
print(check_diagonals(board_7,'X'))

assert (check_rows(board_1,'X') == False)

# check for test caseses