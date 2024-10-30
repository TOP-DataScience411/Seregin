num = int(input())
print(f'Сумма цифр = {int(num/100) + int(int((num%100)/10) + int(num%10))}')
print(f'Произведение цифр = {int(num/100) * int(int((num%100)%10)) * int(num%10)}')

#333
#Сумма цифр = 9
#Произведение цифр = 27