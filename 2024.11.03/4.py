import sys

num = int(sys.stdin.readline().strip())
sum = 0
b = '1' + '0' * (num-1)
b1 = '9' * num
    
for i in range(int(b), int(b1)+1):
    is_prime = True
    for j in range(2,i):
            if i % j == 0: is_prime = False
    if is_prime == True: sum += 1
sys.stdout.write(f"{sum}")