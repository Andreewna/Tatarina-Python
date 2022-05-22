#1.Составить алгоритм:
#если введенное число больше 7, то вывести “Привет”


import keyboard
while True:
    try:
        user_number=int(input("Напишите число:"))
    except:
        print("Введенное значение не является числом")
        exit()
    if user_number >7:
        print( "Привет")
        print("Если хочешь продолжить нажми Entern")
    else:
        print("Введенное значение меньше 7")
        print("Если хочешь продолжить нажми Entern")
    keyboard.record(until='enter')
    






