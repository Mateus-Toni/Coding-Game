import sys
import math

def get_big_mountain(dict_mountain):

    big = 0

    id_mountain = 0

    for key, value in dict_mountain.items():

        if value > big:

            big = value

            id_mountain = key

        
    return id_mountain

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop

while True:

    dict_mountain = {}

    for i in range(8):

        mountain_h = int(input())  # represents the height of one mountain.

        dict_mountain[i] = mountain_h

    print(dict_mountain, file=sys.stderr, flush=True)
    
    id_mountain = get_big_mountain(dict_mountain)

    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    print(id_mountain)
