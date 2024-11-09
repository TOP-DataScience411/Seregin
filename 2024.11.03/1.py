from sys import stdin
from sys import stdout

nums = []
for num in stdin:
    num = num.strip()  
    if int(num) % 7 == 0:
        nums.append(num) 
    else:
        break

for i in range(len(nums) - 1, -1, -1):
    stdout.write(nums[i] + " ")
    
# 7
# 7
# 14
# 21
# 13
# 21 14 7 7