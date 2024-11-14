from sys import stdin
from sys import stdout

nums_1 = list(map(int, stdin.readline().strip().split()))

nums_2 = list(map(int, stdin.readline().strip().split()))

if not nums_2:  
    stdout.write("да\n")
else:

    for i in range(len(nums_1) - len(nums_2) + 1):
        if nums_1[i:i + len(nums_2)] == nums_2:
            stdout.write("да\n")
            break
    else:
        stdout.write("нет\n")


# 1 2 3 4
# 1 2
# да