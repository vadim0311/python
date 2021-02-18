#-----------------------------------------------------------------

# list1 = ['apple', 'pear', 'coconut']

# #печать пункта n
# n = int(input('n-? ' ) )
# print(list1[n ] )

# #замена пункта на значение
# list1[1] = 'CockONut'
# print(list1[n ] )

# #добавить пункт в конце
# list1.append(45)

# #ремув отдельного пункта по номеру ( от нуля !!! )
# del list1[1]
# print(list1[n ] )

# # ремув отдельного пункта по значению
# list1.remove('apple')
# print(list1)



# # SPLIT

# a = input('?: ')
# print(a.split())




# #          СПИСОК ПОКУПОК

# v=0
# i = 0
# list2 = []

# while i == 0:
#     b = input('waka?: ')
#     if b == 'stop':
#         break
#     else:
#         list2.append(b)
#         v +=1

# for i in range(v):
#     print (list2[i], end = '')
#     if i == v-1:
#         pass
#     else:
#         print(', ', end= '')



# # Hor. Diagram 1

# list1 = []

# a = input('split - / : ')
# list1 = a.split('/')

# print('''
#     ''')

# for j in range(len(list1)):
#     print(int(list1[j]) * '|', list1[j])
#     print(int(list1[j]) * '|')
#     print('''
#     ''')



# # Ср Арифм


# list_org = input('wth / ')

# list1 = list_org.split('/')

# sum_marks = 0

# for i in range (len(list1)):
#     sum_marks += int(list1[i])
# print(sum_marks / len)