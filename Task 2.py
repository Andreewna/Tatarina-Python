#2.Составить алгоритм: если введенное имя совпадает с Вячеслав,
#то вывести “Привет, Вячеслав”, если нет, то вывести "Нет такого имени"

name="Вячеслав"
user_name=input("Напиши имя:")

if user_name.capitalize()==name:
    print( "Привет", user_name.capitalize() )
        
else:
    print( "Нет такого имени ")
