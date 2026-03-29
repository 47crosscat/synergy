import math

print(f"\nДобрый день!")
while True:
    getting_number =  input("Введите, пожалуйста, неотрицательное целое число: ")

    try:
        number = int(getting_number)
        
        if number >= 0:
            print(f"\n{number} -- неотрицательное число.")
            print(f"Факториал вашего числа равен \"{math.factorial(number)}\".")
            break
        else:
            print(f"\n\"{number}\" отрицательное число. \nФакториал от отрицательного числа определить невозможно.\n")
    except ValueError:
        print(f"\nВведённое значение \"{getting_number}\" не является неотрицательным целым числом.\n")