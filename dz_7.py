import random

a=[random.randint(0,30) for _ in range(20)]

print(a)
counter=0
for i in range(1,len(a)-1): #Пишем len(a)-1 чтобы убрать крайний эллемент
    if a[i-1] <a[i]>a[i+1]: #Собственно проверка нашего условия
        print(a[i])
        counter+=1
print(counter)


