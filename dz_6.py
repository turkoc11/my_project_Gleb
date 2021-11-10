import random

list_a=[random.randint(1,10) for _ in range(20)]

print(list_a)

list_b=[random.randint(1,10) for _ in range(20)]

print(list_b)

unique_a=list(set(list_a))

unique_b=list(set(list_b))

print(f"Уникальные значения для а:{unique_a}", f"Уникальные значения для b:{unique_b}", len(unique_a),len(unique_b))



