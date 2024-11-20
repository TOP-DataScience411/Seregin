from statistics import median, mean, geometric_mean, harmonic_mean
def central_tendency(num1: float, num2:float, *numbers: float):
# def central_tendency(*numbers: float):
    new_numbers = (num1, num2)
    new_numbers = new_numbers + numbers
        # 'median' — медиана
        # 'arithmetic' — среднее арифметическое
        # 'geometric' — среднее геометрическое
        # 'harmonic' — среднее гармоническое  
    median1  = median(new_numbers) # стандартная функция - для проверки
    median2 = 0                    # ручной расчет
    sort_new_numbers = sorted(new_numbers)
    if len(sort_new_numbers) % 2 != 0:
       median2 = float(sort_new_numbers[int(len(sort_new_numbers) / 2)])
    else:
        median2 = float((sort_new_numbers[int(len(sort_new_numbers) / 2)] + sort_new_numbers[int(len(sort_new_numbers) / 2) - 1]) / 2)
    
    arithmetic1 = mean(new_numbers)
    arithmetic2 = 0
    for i in range(len(new_numbers)):
        arithmetic2 += new_numbers[i]
    arithmetic2 /= len(new_numbers)

    
    geometric1 = geometric_mean(new_numbers)
    geometric2 = 1
    for i in range(len(new_numbers)):
        geometric2 *= new_numbers[i]
    geometric2 = geometric2 ** (1/len(new_numbers))
    
    harmonic1 = harmonic_mean(new_numbers)
    harmonic2 = 0
    for i in range(len(new_numbers)):
        harmonic2 += 1 / new_numbers[i]
    harmonic2 = len(new_numbers) / harmonic2 
    
    cent_tend = {'median' : median2, 'arithmetic' : arithmetic2,'geometric' : geometric2, 'harmonic' : harmonic2}
    return cent_tend
    
# 9:40:13 > python -i 5.py
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}

