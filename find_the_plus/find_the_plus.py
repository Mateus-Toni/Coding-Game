import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = 2
s = 177
o = '44133'

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(n, file=sys.stderr, flush=True)
print(s, file=sys.stderr, flush=True)
print(o, file=sys.stderr, flush=True)

number_1 = int(o[:n])

number_2 = int(o[n:])

if s - number_1 == number_2:

    print(f'{number_2}+{number_2}={s}')

else:

    print("No solution or recovered addition(s)")


lista = ['2', '6', '3', '6', '3', '4', '1', '5', '4', '2', '5', '4', '2', '4', '1', '6', '1', '5', '2', '3', '4', '1', '5', '1', '2', '5', '4', '2', '4', '1']

print(lista.reverse(reversed=True))