import sys

motion1 = sys.stdin.readline().strip()
motion2 = sys.stdin.readline().strip()  

if 1 >=(ord(motion1[0]) - ord(motion2[0])) <= 1 and int(motion1[1]) - int(motion2[1]) <= 1:
    print("да")  
else:
    print("нет") 
    
# c6
# d4
# нет