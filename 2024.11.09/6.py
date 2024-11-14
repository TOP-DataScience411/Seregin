from sys import stdin
from sys import stdout

num = {'0', '1'}

number = stdin.readline().strip()
start = 0

if number.startswith('0b'):
    start = 2
elif number.startswith('b'):
    start = 1

for char in number[start:]: 
    if char not in num:
        stdout.write("нет\n")
        exit()

stdout.write("да\n")


# 1b0101
# нет
