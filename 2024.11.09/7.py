from sys import stdout
import ref7 

dicts = ref7.list_of_dicts  

result = {}

for char in dicts:
    for keys, values in char.items():
        if keys not in result:
            result[keys] = set()
        result[keys].add(values)  


lines = []
for keys, values in result.items():
    lines.append(f"'{keys}': {{{', '.join(map(str, values))}}}")

stdout.write(",\n".join(lines) + "\n")


# 'Владивосток': {5},
# 'Воронеж': {1, 4},
# 'Екатеринбург': {1, 3, 5},
# 'Иркутск': {9, 2, 5},
# 'Москва': {3, 4, 6},
# 'Новокузнецк': {2, 4},
# 'Оренбург': {1},
# 'Саратов': {2},
# 'Уфа': {9},
# 'Ярославль': {8, 7},
# 'Волгоград': {5},
# 'Нижний Новгород': {8, 2, 5},
# 'Ростов-на-Дону': {6},
# 'Тольятти': {1},
# 'Тюмень': {3},
# 'Казань': {4},
# 'Новосибирск': {7},
# 'Пермь': {3},
# 'Челябинск': {3},
# 'Санкт-Петербург': {7}