n1=int(input("Введите 1-ое число: "))#или отдельно через n1=int(n1)
n2=int(input("Введите 2-ое число: "))#или отдельно через n2=int(n2)

print("n1 =", type(n1))
print("n2 =", type(n2))

if n1 > n2:
    print(n1, "- самое большое число из перечисленных.")
elif n1==n2:   
    print("Числа", n1, "и", n2, "равны")
else:
    print(n2, "- самое большое число из перечисленных.")