import random

random_number = random.randint(1,100)
attempts = 8

# print(f"Случайное число: {random_number}")
print(f"\nПривет!\n\nДавай сыграем в игру \"Угадай число\".\n\nКомпьютер случайным образом выбрал число в диапазоне от 1 до 100.\nПравила такие: если ты не угадываешь, или вводишь число не из диапазона, или не число, или даже отправляешь пустоту -- число попыток уменьшается на одну, всего их {attempts}.\nУдачи!\n\nИтак, компьютер загадал число. ")


while attempts > 0:
    user_number = input("\nВведи свой вариант числа: ")

    try:
        check_number = int(user_number)

        if check_number >= 1 and check_number <= 100:

            if check_number < random_number:
                attempts -= 1
                print(f"\nТвоё число меньше загаданного.\nПопыток осталось всего: {attempts}.\n")
            elif check_number > random_number:
                attempts -= 1
                print(f"\nТвоё число больше загаданного.\nПопыток осталось всего: {attempts}.\n")
            else:
                print(f"\nЙей! Ты угадал! Это действительно число {user_number}!\nИ на угадывание у тебя ушло вот сколько попыток: {attempts}.")
                break

        else:
            attempts -= 1
            print(f"Введи число в диапазоне от 1 до 100.\nПопыток осталось всего: {attempts}.\n")

    except ValueError:
        attempts -= 1
        print(f"\nНо ведь \"{user_number}\" не является целым числом.\nПопыток осталось всего: {attempts}.\n")

    if attempts == 1:
        print(f"Последняя попытка! Посмотри в {random_number-1} -- {random_number+1}")
    elif attempts == 0:
        print(f"Игра окончена.\nИскомое число: {random_number}")