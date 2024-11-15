from sys import stdin
from sys import stdout  
import ref5

ref5 = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

word = stdin.readline().strip()

key = 0

for char in word.upper():  
    for scores, values in ref5.items():
        if char in values:
            key += scores
            break 

stdout.write(str(key) + "\n")


# синхрофазотрон
# 29