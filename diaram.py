# a = input('(with /) ?: ')
# list1 = a.split('/')
# list1 = [int(x) for x in list1]
# list1.sort(reverse = True)
# print(list1)

list1 = []
i1 = 0

while i1 == 0:
    a = input('? ')
    if a == 'stop':
        i1 += 1        
    else:
        list1.append(int(a))

h = max(list1)
k = h

print('#', '# ' * len(list1), end = '')
print('#')

for i2 in range(h):
    print('# ', end = '')
    for j in range(len(list1)):
        if list1[j] >= k:
            print('* ', end = '')
        else:
            print('- ', end = '')
    print('# ', end = '')
    print('')
    k -= 1

print('# ' * (len(list1) + 2))