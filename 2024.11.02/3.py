import sys

year = int(sys.stdin.readline().strip()) 

if (year % 4) == 0 and not (year % 100) == 0 or (year % 400) == 0:
    print("да") 
else:
    print("нет") 

# 2020
# да
