Sum=0
y=0

while y==0:
    x=int(input('''
--------
1-перечисляет числа от a до b 
2-перечисляет чётные числа от a до b
3-перечисляет нечётные числа от a до b
4-сумма арифметической прогрессии a, b 
5-перечисляет числа от a до b, которые делятся на c
6-конец
--------
    '''))

    if x == 1:
        a=int(input('a '))
        b=int(input('b '))
        for i in range(a, b+1):
            print(i)

    elif x == 2:
        a=int(input('a '))
        b=int(input('b '))
        for i in range(a, b+1):
            if i%2 == 0 and i != 0:
                print(i)
            else:
                pass

    elif x == 3:
        a=int(input('a '))
        b=int(input('b '))
        for i in range(a, b+1):
            if i%2 == 1 and i != 0:
                print(i)
            else:
                pass

    elif x == 4:
        a=int(input('a '))
        b=int(input('b '))
        for i in range(a, b+1):
            Sum=Sum+i
        print(Sum)

    elif x == 5:
        a=int(input('a '))
        b=int(input('b '))
        c=int(input('c '))
        for i in range(a, b+1):
            if i%c == 0 and i != 0:
                print(i)
            else:
                pass
    elif x == 6:
        y+=1
    else:
        pass
