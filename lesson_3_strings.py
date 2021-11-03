my_string = str(input("Введите вашу строчку"))
print(my_string)
# Input нужен для ввода текста с клавиатуры,поскольку у нас строка указываем строковый тип данных

program_string = f"Вы написали {my_string} в  свою строку "

print(program_string)

# Выводим нашу измененную строчку на экран

program_string = program_string.replace(my_string,"Новая строка")

print(program_string)


print(len(program_string))

if "строка" in program_string:
    print("Да")
elif "строку" in program_string:
    print('''Да,но слово "строку",а не "строка ''')
else:
    print("Нет")
