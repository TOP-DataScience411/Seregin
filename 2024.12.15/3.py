class ChessKing:
    ranks = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}
    files = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    def __init__(self, color='white', square=None):
        self.color = color
        if square is None:
            if color == 'white':
                self.square = 'e1'
            else:
                self.square = 'e8'
        else:
            self.square = square

    def __repr__(self):
        return f"{self.color[0].upper()}K: {self.square}"

    def is_turn_valid(self, new_square):
        current_file = self.files[self.square[0]]
        current_rank = self.ranks[self.square[1]]
        new_file = self.files[new_square[0]]
        new_rank = self.ranks[new_square[1]]

        return abs(current_file - new_file) <= 1 and abs(current_rank - new_rank) <= 1

    def turn(self, new_square):
        if self.is_turn_valid(new_square):
            self.square = new_square
        else:
            raise ValueError('Невозможно выполнить ход')
            
            
# > python -i 3.py
# >>> wk = ChessKing()
# >>> wk.color
# 'white'
# >>> wk.square
# 'e1'
# >>>
# >>> wk.turn('e2')
# >>> wk
# WK: e2
# >>> wk.turn('d4')
    # raise ValueError('Невозможно выполнить ход')
# ValueError: Невозможно выполнить ход
# >>> bk = ChessKing('black')
# >>> print(bk)
# BK: e8
# >>>

