def deck():
    suit = ('черви', 'бубны', 'пики', 'трефы')
    for i in range(len(suit)):
        for j in range(2, 15):
            yield (j, suit[i])
        
  

# python -i 1.py
# >>> list(deck())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]

            