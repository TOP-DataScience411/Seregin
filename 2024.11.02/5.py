import sys

motion1 = sys.stdin.readline().strip() 
motion2 = sys.stdin.readline().strip()  

if motion1[0] == motion2[0] or motion1[1] == motion2[1]:
     sys.stdout.write("да") 
else:
     sys.stdout.write("нет") 
     
# d4
# e4
# да
