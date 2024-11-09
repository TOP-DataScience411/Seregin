import sys

n = int(sys.stdin.readline().strip())

a = a1 = 1

sys.stdout.write(str(a) + ' ')

if n > 1:

    sys.stdout.write(str(a) + ' ')

for i in range(2, n):
    a, a1 = a1, a + a1
    sys.stdout.write(str(a1) + ' ')
