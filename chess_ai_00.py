from copy import deepcopy

# todo shallow_blue: pawn wars?

# checkers
boardT = [[1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [2, 2, 2, 2, 2, 2],
         [2, 2, 2, 2, 2, 2]]

boardS = [[ 1,  1,  1,  1,  1],
          [ 0,  0,  0,  0,  0],
          [ 0,  0,  0,  0,  0],
          [-1, -1, -1, -1, -1]]

ConnectFour = [[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]

#agenda = [board]

# populate agenda
# find nodes
# expand nodes
# add to agenda


# min/max recursion (maximizing):
    # if bottom level is reached or terminal node:
        # return heuristic


    # if maximizing player:

        # (pick path that minimizes loss)
        # search level
        #
        # recurse until bottom level

#print float('inf')


def minimax(node, depth, maximizing_player):
    node_children = moves(node, maximizing_player)

    if depth == 0 or node_children == []:  # or game over?
        return heuristic_value(node, maximizing_player), node

    if maximizing_player:
        best_value = -float('inf')
        best_move = None
        for each_child in node_children:
            value = minimax(each_child, depth - 1, False)
            if value[0] > best_value:
                best_value = value[0]
                best_move = value[1]
            print "max value:\t\t", value
        print "max best:\t\t", best_value, best_move
        print "depth:", depth, "\n"
        return best_value, best_move

    else:  # not maximizing_player:
        best_value = float('inf')
        best_move = None
        for each_child in node_children:
            value = minimax(each_child, depth - 1, True)
            if value[0] < best_value:
                best_value = value[0]
                best_move = value[1]
            print "not-max value:\t", value
        print "min best:\t\t", best_value, best_move
        print "depth:", depth, "\n"
        return best_value, best_move


def heuristic_value(node, maximizing_player):
    if False:
        counter_ones = 0
        counter_twos = 0
        board_position_ones = 0
        board_position_twos = 0
        for i in range(len(node)):
            for j in range(len(node[0])):
                # score based on number of pieces and those pieces nearness to the other side of the board
                if node[i][j] == 1:
                    counter_ones += 1
                    board_position_ones += 1*(i+1)
                    if i == 2 and j == 2:
                        board_position_ones += 3
                if node[i][j] == -1:
                    counter_twos += 1
                    board_position_twos += 1*(len(node[0])-i)
                    if i == 2 and j == 2:
                        board_position_twos += 3

        if maximizing_player:
            capture_bonus = (12 - counter_twos)*12  # todo hardcoded
            capture_bonus = 0
            counter = counter_ones + board_position_ones + capture_bonus
            #counter = counter_ones - counter_twos

        else:  # (not maximizing_player)
            capture_bonus = (12 - counter_ones)*12  # todo hardcoded
            capture_bonus = 0
            counter = counter_twos + board_position_twos + capture_bonus
            #counter = counter_twos - counter_ones
            counter = -counter

    counter = 0
    for i in range(len(node)):
        for j in range(len(node[0])):
            if maximizing_player:
                player_value = 1
            else:
                player_value = -1
            if node[i][j] == player_value:
                counter += 1
    if not maximizing_player:
        counter = -counter

    return counter  #_ones, counter_twos  # could evaluate only one number for speed


def moves(board_m, maximizing_player):
    node_children = []
    if maximizing_player:
        current_player = 1
        opposite_player = -1
        forward = 1
    else:
        current_player = -1
        opposite_player = 1
        forward = -1
    # search for node children (allowed moves)
    for i in range(len(board_m)):
        for j in range(len(board_m[0])):
            # if correct player
            if (i + forward) < len(board_m) and board_m[i][j] == current_player:
                # move forward
                if board_m[i+forward][j] == 0:
                    child = deepcopy(board_m)
                    child[i+forward][j] = current_player
                    child[i][j] = 0
                    node_children.append(child)
                # capture (pawn capture)
                if (j + forward) < len(board_m[0]) and board_m[i+forward][j+forward] == opposite_player:
                    child = deepcopy(board_m)
                    child[i+forward][j+forward] = current_player
                    child[i][j] = 0
                    node_children.append(child)
                if (j - forward) < len(board_m[0]) and board_m[i+forward][j-forward] == opposite_player:
                    child = deepcopy(board_m)
                    child[i+forward][j-forward] = current_player
                    child[i][j] = 0
                    node_children.append(child)
    return node_children



def pretty_print(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            #if j == len(board)-1:
            #    print board[i][j]
            #else:
            #    print board[i][j], "",
            #if j == 0:
            '''
            if (i == 0 and j == 0):  # or (i == len(board[0]) - 1 and j == len(board[0]) - 1):
                hor = " "
                for each in range(len(board)*3-1):
                    hor += "-"
                print hor
            '''
            if j == 0:
                print "|",
            if board[i][j] == 0:
                print " ",
            if board[i][j] == 1:
                print "x",
            if board[i][j] == -1:
                print "o",
            if j == len(board[0]) - 1:
                print "|"
    '''
    hor = " "
    for each in range(len(board) * 3 - 1):
        hor += "-"
    print hor
    '''

    return

'''
for each in moves(board, True):
    pretty_print(each)
    print
'''

#print heuristic_value(board)

search_result = minimax(boardS, 2, True)
print "\nminimax(boardS, 2, True):\n", search_result[0], search_result[1]
print "\nsearch_result[1]"
pretty_print(search_result[1])


'''
test = [[1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1],
        [0, 2, 1, 0, 0, 0],
        [0, 0, 0, 2, 0, 0],
        [2, 2, 0, 0, 2, 2],
        [2, 2, 2, 2, 2, 2]]


print heuristic_value(test, False)
'''
