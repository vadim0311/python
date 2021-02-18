import random
n=random.randint(1, 100)
x=1
print('please input number(1-100): ')
while x==1:
    a=int(input(''))
    c=1488
    if a==n:
        print('congrats ')
    elif n-2 < a < n+2: 
        print('closeer ')
    elif a<n+5 and a>n-5:
        print('closer ')
    elif a<n+20 and a>n-20:
        print('warm ')
    elif a==c:
        print(n)
    else:
        print('cold ')