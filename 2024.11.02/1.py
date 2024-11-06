import sys

total_sum = 0.0  


for i in range(3):
    line = sys.stdin.readline()  
    number = float(line.strip()) 

    if number > 0: 
        total_sum += number  

print(total_sum)

# 4
# -22
# 1.5
# 5.5
