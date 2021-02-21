import random
y=1
while y==1:
    v=int(input('''
    Какой вариант выберете?
    1)1-100 2)1-1000
    '''))
    if v==1:
        n=random.randint(1, 100)
        x=1
        print('''
    Мы загадали число от 1 до 100
    Попробуйте угадать его!
    ''')
        while x==1:
            a=int(input(''))
            if a==n:
                print('congrats')
                x=0
            elif a<n+5 and a>n-5:
                print('close')
            elif a<n+20 and a>n-20:
                print('warm')
            else:
                print('cold')
        z=input('Do you want to continue? Y/N ')
        x2=1
        while x2==1:
            if z=='Y' or z=='y':
                y=1
                x2=0
            elif z=='N' or z=='n':
                y=0
                x2=0
            else:
                pass
    elif v==2:
        n=random.randint(1, 1000)
        x=1
        print('''
        Мы загадали число от 1 до 1000
        Попробуйте угадать его!
        ''')
        while x==1:
            a=int(input(''))
            if a==n:
                print('congrats')
                x=0
            elif a<n+10 and a>n-10:
                print('close')
            elif a<n+20 and a>n-20:
                print('warm')
            elif a<n+50 and a>n-50:
                print('warm')
            elif a<n+100 and a>n-100:
                print('warm')
            else:
                print('cold')
        z=input('Do you want to continue? Y/N ')
        x2=1
        while x2==1:
            if z=='Y' or z=='y':
                y=1
                x2=0
            elif z=='N' or z=='n':
                y=0
                x2=0
            else:
                pass
    else:
        print('please write the number')      