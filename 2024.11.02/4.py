import sys

cell1 = sys.stdin.readline().strip() 
cell2 = sys.stdin.readline().strip()  

if (ord(cell1[0]) + int(cell1[1]) + ord(cell2[0]) + int(cell2[1])) % 2 == 0:
    print("да")  
else:
    print("нет") 

# a1
# b2
# да