import sys
import math

# Save humans, destroy zombies!

def get_x(coord):

    pass


def get_y(coord):

    pass

def get_most_danger(x, y, list_human, list_zombie):

    for human in list_human:

        for zombie in list_zombie:

            pass

# game loop
while True:

    list_human = []
    list_zombie = []

    x, y = [int(i) for i in input().split()]
    
    human_count = int(input())
    
    for i in range(human_count):
        
        human_id, human_x, human_y = [int(j) for j in input().split()]
        
        list_human.append([human_id, human_x, human_y])

    zombie_count = int(input())

    for i in range(zombie_count):

        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        
        list_zombie.append([zombie_id, zombie_x, zombie_y])

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Your destination coordinates
    print("0 0")