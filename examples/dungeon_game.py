import os
import random

# draw grid
# pick random location for the player
# pick random location for exit door
# pick random location for the monster
# draw player in the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw grid

# 5 * 5
# CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
#          (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
#          (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
#          (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
#          (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), ]
CELLS = [(x, y) for y in range(5) for x in range(5)]
print(CELLS)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_locations():
    return random.sample(CELLS, 3)  # 重複無し（母集団に重複がある場合は、それぞれが1回ずつ出現する可能性がある）


def move_player(player, move):
    # get the player position
    x, y = player
    # move
    if move == 'LEFT':
        x -= 1
    if move == 'RIGHT':
        x += 1
    if move == 'UP':
        y -= 1
    if move == 'DOWN':
        y += 1

    return x, y  # pack to a tuple


# get valid moves
def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = player

    # alongside the wall?
    if x == 0:
        moves.remove('LEFT')
    if x == 4:
        moves.remove('RIGHT')
    if y == 0:
        moves.remove('UP')
    if y == 4:
        moves.remove('DOWN')

    return moves


def draw_map(player):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            output = tile.format("X") if cell == player else tile.format("_")
        else:  # x == 4
            line_end = "\n"
            output = tile.format("X|") if cell == player else tile.format("_|")
        print(output, end=line_end)


def game_loop():
    monster, door, player = get_locations()
    playing = True

    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)

        # print the player's position
        print("You're currently in room {}".format(player))
        # print the available moves
        print("You can move [{}]".format(", ".join(valid_moves)))
        print("Enter 'QUIT' to quit")

        move = input("> ").upper()

        if move == 'QUIT':
            print("\n ** See you next time! **\n")
            break
        if move in valid_moves:
            player = move_player(player, move)

            if player == monster:
                print("\n ** Oh no! The monster got you! Better luck next time! **\n")
                playing = False
            if player == door:
                print("\n ** You escaped! Congratulations! **\n")
                playing = False
        else:
            input("\n ** Walls are hard! Don't run into them! **\n")
    else:
        if input("Play again? [Y/n] ").lower() == "n":
            print("\n ** See you next time! **\n")
        else:
            game_loop()


if __name__ == '__main__':
    clear_screen()
    print("Welcome to the dungeon!!")
    input("Press ENTER to start!")
    clear_screen()
    game_loop()
