from sys import stdin
from sys import stdout

n = int(stdin.readline().strip())
positive_sum = 0

for _ in range(n):
    num = int(stdin.readline().strip())
    if num > 0:
        positive_sum += num

stdout.write(str(positive_sum) + '\n')

# 6
# 3
# -5
# 1
# 10
# -1
# 8
# 22
