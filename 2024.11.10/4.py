def countable_nouns(number, words=tuple[str, str, str]):
    if not isinstance(number, int):
        return None  

    char = 2  

    if number % 10 == 1 and number % 100 != 11:
        char = 0  
    elif 10 <= number % 100 <= 20:
        char = 2  
    elif number % 10 in [2, 3, 4]:
        char = 1  

    return words[char]  


# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'
# >>>