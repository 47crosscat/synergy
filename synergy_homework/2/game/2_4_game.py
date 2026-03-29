import random

random_number = random.randint(1,100)
attempts = 8

# print(f"Случайное число: {random_number}")
print(f"\nДобрый день!\n\nДавайте сыграем в игру \"Угадай число\".\nЧисло выбрано случайным образом в диапазоне от 1 до 100.\nЧисло попыток: {attempts}\n")


while attempts > 0:
    user_number = input("Введите свой вариант числа: ")

    try:
        check_number = int(user_number)

        if check_number >= 1 and check_number <= 100:

            if check_number < random_number:
                attempts -= 1
                print(f"Ваше число меньше загаданного.\nКоличество оставшихся попыток: {attempts}.\n")
            elif check_number > random_number:
                attempts -= 1
                print(f"Ваше число больше загаданного.\nКоличество оставшихся попыток: {attempts}.\n")
            else:
                print(f"Ура! Это действительно число {user_number}!")
                break

        else:
            attempts -= 1
            print(f"Введите число в диапазоне от 1 до 100.\nКоличество оставшихся попыток: {attempts}.\n")

    except ValueError:
        attempts -= 1
        print(f"\nВведённое значение \"{user_number}\" не является целым числом.\nКоличество оставшихся попыток: {attempts}.\n")

    if attempts == 0:
        print(f"Игра окончена.\nИскомое число: {random_number}")