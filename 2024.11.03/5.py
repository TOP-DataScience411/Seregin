from sys import stdin

text = stdin.readline().strip()

n = len(text) - text.count(' ')

s = n * 30
rub = s // 100
kop = s % 100

print(f'{rub} руб. {kop} коп.')
