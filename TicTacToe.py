def win_condition(player, game_playing):
    if grid[0] == [player, player, player]:
        winner = player
        game_playing = False
        return(winner, game_playing)
    elif grid[1] == [player, player, player]:
        winner = player
        game_playing = False
        return(winner, game_playing)
    elif grid[2] == [player, player, player]:
        winner = player
        game_playing = False
        return(winner, game_playing)
    elif grid[0][0] == grid[1][0] == grid [2][0] == player:
        winner = player
        game_playing = False
        return(winner, game_playing)
    elif grid[0][1] == grid[1][1] == grid [2][1] == player:
        winner = player
        game_playing = False
        return(winner, game_playing)
    elif grid[0][2] == grid[1][2] == grid [2][2] == player:
        winner = player
        game_playing = False
        return(winner, game_playing)
    elif grid[0][0] == grid[1][1] == grid [2][2] == player:
        winner = player
        game_playing = False
        return(winner, game_playing)
    elif grid[0][2] == grid[1][1] == grid [2][0] == player:
        winner = player
        game_playing = False
        return(winner, game_playing)
    else:
        winner = None
        game_playing = True
        return(winner, game_playing)

def player_switch (player):
    if player == 'X':
        player = 'O'
        return player
    else:
        player = 'X'
        return player

def print_grid (grid):
    for row in grid:
        for number in row:
            print(number, end=' ')
        print()

game_playing = True
player = 'X'
winner = None

grid = [['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']]

print_grid(grid)

while game_playing == True:
    try:
        #Asks for position to put an X or an O into the grid
        position = input(f'Player {player} input a coordinate (row,column), where you would like to play: ')
        position_values = position.split(',')
        row = int(position_values[0])-1
        column = int(position_values[1])-1

        #Condition to meet if a player has already played in the position
        if grid[row][column] == '_':
            grid[row][column] = player
        else:
            print('Someone has already played there')
            continue

        print_grid(grid)
        next_player = player_switch (player)
        winner, game_playing = win_condition(player, game_playing)

        if game_playing == True and winner == None:
            player = next_player
        else:
            print(f'Winner is player {player}')
            break

        #Conditions to meet for a tie. Checks for any _ in the grid
        if all('_' not in position for position in grid):
            print('Tie Game!')
            break

    except:
        print('Input number between 1-3 for both positions, separated by a comma')