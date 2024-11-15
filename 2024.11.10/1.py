def strong_password(password):
    if len(password) >= 8:
    
        digit_count = 0
        upper = False
        lower = False
        symbol = False

        for char in password:
            if char.isdecimal() and digit_count < 2:
                digit_count += 1

    for char in password:
        if char.isdigit():
            digit_count += 1
        elif char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif not char.isalnum():
            has_symbol = True

    return (digit_count >= 2 and upper and lower and symbol)


 # 16:33:30 > python -i 1.py
# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password')
# False
# >>>