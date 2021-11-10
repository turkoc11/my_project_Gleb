import random

list_height=[random.randint(150,200) for _ in range (30)]

height_Petya=int(input("Введите рост пети"))

list_height.append(height_Petya)

list_height.sort(reverse=True)
print(list_height)

position_Petya=0

while position_Petya<len(list_height) and list_height[position_Petya]>=height_Petya:
    position_Petya+=1

print(f"Петина позиция будет под номером {position_Petya}")