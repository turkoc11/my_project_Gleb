variable = 478

hundreds = variable // 100

# Чтобы выделить сотни, нужно взять целую часть от деления на 100

tens = (variable % 100) // 10

'''
Чтобы выделить десятки,нужно взять остаток от деления на 100, 
после чего выделить целую часть от данного остатка путем деления числа на 10
'''

units = variable % 10

# Чтобы выделить единицы,нужно взять остаток от деления на 10

print(units, tens, hundreds)

# Так мы не получим само число,а лишь в терминале 3 отдельных

over_variable = units*100 + tens*10 + hundreds

print(over_variable)

'''Завели новую переменную,которая и будет нашим обратным числом.
Умножаем единицы на 100,чтобы они стали первыми
Десятки на 10
Сотни лишь прибавляем'''




