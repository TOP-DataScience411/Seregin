from sys import stdin
from sys import stdout

num = 0
sum = 0

for n in stdin:
    num = int(n)
    break
    
for i in range(int(num / 2)):
    if num % (i + 1) == 0:
        sum += (i + 1)

sum += num
stdout.write(str(sum))

# 76
# 140