# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x or y or z)) == (not x and not y and not z):
                print(f'Для значений: x = {x}, y = {y}, z = {z} утверждение ИСТИННО!')
            else:
                print(f'Для значений: x = {x}, y = {y}, z = {z} утверждение ЛОЖНО!')