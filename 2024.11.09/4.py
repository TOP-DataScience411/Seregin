from sys import stdout
from sys import stdin

error_list = []

for line in stdin:
    line = line.strip()
    if line:  
        code, name = line.split(maxsplit = 1)  
        error_list.append((name, code))  
    else:
        break

error_name = stdin.readline().strip()  

for name, code in error_list:
    if name == error_name:
        stdout.write(code + "\n") 
        break
else:
    stdout.write("! value error !\n") 
    
    
    # 1004 ER_CANT_CREATE_FILE
    # 1005 ER_CANT_CREATE_TABLE
    # 1006 ER_CANT_CREATE_DB
    # 1007 ER_DB_CREATE_EXISTS
    # 1008 ER_DB_DROP_EXISTS
    # 1010 ER_DB_DROP_RMDIR
    # 1016 ER_CANT_OPEN_FILE
    # 1022 ER_DUP_KEY

    # ER_CANT_CREATE_DB
# 1006

