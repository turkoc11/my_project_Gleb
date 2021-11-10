import random

list_a=[random.randint(1,10) for _ in range(20)]

print(list_a)

list_b=[random.randint(1,10) for _ in range(20)]

print(list_b)
count=0
count1=0
unique_b=[]
unique_a=[]
for i in list_a:
    if i not in unique_a:
        count=count+1
        unique_a.append(i)
for j in list_b:
    if j not in unique_b:
        count1=count1+1
        unique_b.append(j)

print(unique_a, unique_b, count, count1)





