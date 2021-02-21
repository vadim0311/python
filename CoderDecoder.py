
var = int(input('''
-------
choose the variant
1 - Code
2 - Decode
------- 
'''))

if var == 1:
    a = input('Enter: ')
    i = 0
    n = int(input('key: '))
    if n > 0:  
        while i != len(a):
            print(chr( ord(a[i]) + n), end = '')
            i += 1
    else:
        print('no')
elif var == 2:
    var2 = int(input('''
-------
choose the variant
1 - Decode
2 - MegaAutoDecoder2.0
------- 
'''))
    if var2 == 1:
        a = input('Enter: ')
        i = 0
        n = int(input('key: '))
        if n > 0:  
            while i != len(a):
                print(chr( ord(a[i]) - n), end = '')
                i += 1
        else:
            print('no')
    elif var2 == 2:
        a = input('Enter: ')
        x = int(input('First num of key?'))
        y = int(input('Last num of key?'))
        for n in range(x, y):
            i = 0
            print('''
''')
            while i != len(a):
                print(chr( ord(a[i]) - n), end = '')
                i += 1
    else:
        print('no')
else:
    print('die')