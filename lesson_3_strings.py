my_string = str(input("Введите вашу строчку"))
print(my_string)
# Input нужен для ввода текста с клавиатуры,поскольку у нас строка указываем строковый тип данных

program_string = "Вы написали в свою строку {}".format(my_string)

print(program_string)

# Выводим нашу измененную строчку на экран

my_string = "замена в строке"

program_string = "Вы заменили свою строку на {}".format(my_string)

print(program_string)

print(len(program_string))

if "строка" in program_string:
    print("Да")
elif "строку" in program_string:
    print('''Да,но слово "строку",а не "строка ''')
else:
    print("Нет")
