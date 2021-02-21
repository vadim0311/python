list1 = []
print('type 0 to quit')
while True:
    a = input('? ')
    a = int(a)
    if a == 0:
        break
    elif a >= 1000:
        a = a/100*95
        list1.append(a)
    else:
        list1.append(a)
print(sum(list1))        
