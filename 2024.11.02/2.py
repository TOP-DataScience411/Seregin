import sys

num1 = int(sys.stdin.readline().strip())  
num2 = int(sys.stdin.readline().strip())  

if num1 % num2 == 0:
    print(f'{num1} делится на {num2} нацело \nчастное: {num1//num2}')
else:
    print(f'{num1} не делится на {num2} нацело \nнеполное частное: {num1//num2}\nостаток: {num1%num2%num2}')
    
# 8
# 2
# 8 делится на 2 нацело
# частное: 4
