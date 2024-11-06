import sys

motion1 = sys.stdin.readline().strip() 
motion2 = sys.stdin.readline().strip()  

if motion1[0] == motion2[0] or motion1[1] == motion2[1]:
    print("да") 
else:
    print("нет") 
