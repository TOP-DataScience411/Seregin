from sys import stdin, stdout


fruits = []
for line in stdin:
    fruit = line.strip()
    if fruit:  
        fruits.append(fruit)
    else:
        break

if not fruits:
    result = ""
elif len(fruits) == 1:
    result = fruits[0]
elif len(fruits) == 2:
    result = " и ".join(fruits)
else:
    result = ", ".join(fruits[:-1]) + " и " + fruits[-1]

stdout.write(result + "\n")


# груша
# лимон
# апельсин
# яблоко

# груша, лимон, апельсин и яблоко
