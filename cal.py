# per=1
# while per==1:
#     NAME=input("Введите имя: ")
#     while per==1:
#         con=input("Уверены? Y/N: ")
#         if con=="Y" or con=="y":
#             print("Значит", NAME, "...")
#             per=0
#         elif con=="N" or con=="n":
#             print('...')
#         else:
#             print("you should type Y or N!")

start=int(input('''
Выберите точку старта? (напишите число)

1-Правен      2-Ельфийский лес
3-Дикие земли 4-Горы гномов
'''))

if start == 1:
    dest=int(input('''
Вы находите себя блуждающим по площади некого города, который вы видите впервые
Вокруг бродят люди: бедняки, наемники с оружием и проезжают кареты с телег.
Над хлиплыми деревянными домами возвышался красивый замок с мощными стенами.
По направлению потока людей вы отыскали неывсокие деревянные городские ворота.

Вы не знаете кто Вы, и почему Вы здесь.
Видимо нужно начинать жизнь с нуля...

            И вы принимаете решение...
1-пройтись до замка      2-Исследовать город и дальше
3-Идти к воротам
    '''))
    if dest==1:
        d1=int(input(''' 
Подойдя к воротам замка, вы видите тучного вида мужчину, охраняющего ворота.
Может он что-нибудь рассказажет о городе?
1-Расспросить его         2-Пойти назад 
'''))
        if d1==1:
            print('''
Из ,с явным нежелание поведанного, рассказа стражника вы узнаёте, что "имеете честь" находиться в городе Правен.
Правен - столица королевства людей Ракалии, которое граничит с лесом эльфов на юге, горами гномов на востоке, 
и обширными дикими землями на западе.
Узнав, что вы не знаете даже кто вы такой и, разумеется, не имеете ни гроша в кармане, стражник, подметив,
что вы выглядите довольно здоровым и сильным (что довольно редко для простолюдинов людской расы)
советует вам сходить в гильдию наёмников, чтобы зароботать денег.
            ''')
            print("Так, вы направились в сторону, указанную стражником...")
        else:
            print('sd')
    else:
        print('sd')
else:
    print('sd')