y=0
while y==0:
    a=int(input('a '))
    b=int(input('b '))
    x=int(input('''
---
Выберите номер действия
1- Вычитание            3- Деление
2- Сложение             4- Умножение
5- Выход
---
    '''))
    if x==2:
        def sum(a,b):
            return a+b
        print(sum(a,b))
    elif x==1:
        def sub(a,b):
            return a-b
        print(sub(a,b))
    elif x==3:
        def mul(a,b):
            return a*b
        print(mul(a,b))
    elif x==4:
        def div(a,b):
            return a/b
        print(div(a,b))
    elif x==5:
        y+=1
    else:
        print('kek')