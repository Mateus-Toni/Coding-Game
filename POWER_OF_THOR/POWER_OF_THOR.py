import sys
import math

def get_coord(light_x, light_y, initial_tx, initial_ty):

    coord = ''

    if light_x == initial_tx or light_y == initial_ty:

        if light_y == initial_ty:

            value = initial_tx - light_x

            if value > 0:

                initial_tx -= 1

                coord = 'W'

            else:
                
                initial_tx += 1

                coord = 'E'


        elif light_x == initial_tx:

            value = initial_ty - light_y

            if value > 0:

                initial_ty -= 1

                coord = 'N'

            else:

                initial_ty += 1

                coord = 'S'

    else:

        value_x = initial_tx - light_x

        value_y = initial_ty - light_y

        if value_x > 0:

            initial_tx -= 1

            coord_x = 'W'

        else:

            initial_tx += 1

            coord_x = 'E'

        if value_y > 0:

            initial_ty -= 1

            coord_y = 'N'
            
        else:

            initial_ty += 1

            coord_y = 'S'

        coord = coord_y + coord_x

    

    return coord, initial_ty, initial_tx


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    # print(light_x, file=sys.stderr, flush=True)
    # print(light_y, file=sys.stderr, flush=True)
    # print(initial_tx, file=sys.stderr, flush=True)
    # print(initial_ty, file=sys.stderr, flush=True)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    for turn in range(remaining_turns):
        
        coord, initial_ty, initial_tx = get_coord(light_x, light_y, initial_tx, initial_ty)
        print(coord)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    
        