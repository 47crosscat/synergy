def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

getting_number = input("Добрый день!\nВведите, пожалуйста, число: ")

try:
    number = int(getting_number)
    if number >= 0:
        print(f"\n{number} -- неотрицательное число.")
        print(f"Факториал вашего числа равен \"{factorial(number)}\".")
    else:
        print(f"\n\"{number}\" отрицательное число. \nФакториал от отрицательного числа определить невозможно.")
except ValueError:
    print(f"\nВы ввели: \"{getting_number}\", это не число.")