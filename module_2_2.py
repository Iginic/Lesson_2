first = int(input('Введите чило №1 :'))
second = int(input('Введите чило №2 :'))
third = int(input('Введите чило №3 :'))
if first == second and first == third:
    print(3)
elif first == second or first == third:
    print(2)
elif first != second or first != third:
    print(0)
