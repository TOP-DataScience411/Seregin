def orth_triangle(cathetus1: float = 0, cathetus2: float = 0, hypotenuse: float = 0):

    # print(cathetus1, cathetus2, hypotenuse)   
    if cathetus1 > 0 and cathetus2 > 0 and hypotenuse > 0:
        return None
    if cathetus1 < 0 or cathetus2 < 0 or hypotenuse < 0:
        return None
    if hypotenuse > 0 and (hypotenuse < cathetus1 or hypotenuse < cathetus2): 
        return None
    
    if hypotenuse == 0:
        hypotenuse = (cathetus1 ** 2 + cathetus2 ** 2) ** (1/2)
        return hypotenuse
    elif cathetus1 > 0:
        cathetus2 =  (hypotenuse ** 2 - cathetus1 ** 2) ** (1/2)
        return cathetus2
    else: 
        cathetus1 = (hypotenuse ** 2 - cathetus2 ** 2) ** (1/2)
        return cathetus1

  # 9:45:34 > python -i 6.py
# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None
# >>>
