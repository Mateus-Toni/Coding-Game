import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.

def get_y(min_y, y, bomb, y0):
        
    if 'U' in bomb:
        
        y = y0 - 1 
    
    elif 'D' in bomb:
        
        min_y = y0 + 1 

    y0 = round((y + min_y) / 2)
        
    return min_y, y, y0
    

def get_x(min_x, x, bomb, x0):
        
    if 'R' in bomb:
        
        min_x = x0 + 1
    
    elif 'L' in bomb:
        
        x = x0 - 1

    x0 = round((x + min_x) / 2)
     
    return min_x, x, x0

w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
min_x = 0
min_y = 0
w = w-1
h = h-1
# game loop
while True:
    
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    print(bomb_dir, file=sys.stderr, flush=True)
    print(w, file=sys.stderr, flush=True)
    print(h, file=sys.stderr, flush=True)
    print(min_x, file=sys.stderr, flush=True)
    print(min_y, file=sys.stderr, flush=True)
    
    min_y, h, y0 = get_y(min_y=min_y, y=h, bomb=bomb_dir,y0=y0)
    min_x, w, x0 = get_x(min_x=min_x, x=w, bomb=bomb_dir,x0=x0)
        
    print(bomb_dir, file=sys.stderr, flush=True)
    print(w, file=sys.stderr, flush=True)
    print(h, file=sys.stderr, flush=True)
    print(min_x, file=sys.stderr, flush=True)
    print(min_y, file=sys.stderr, flush=True)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
    
    print(f'{x0} {y0}')