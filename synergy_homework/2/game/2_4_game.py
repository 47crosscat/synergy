import random

random_number = random.randint(1,100)
max_attempts = 8
attempts = max_attempts

print(f"\nПривет!\n\nДавай сыграем в игру \"Угадай число\".\n\nКомпьютер случайным образом выбрал число в диапазоне от 1 до 100.\nПравила такие: если ты не угадываешь, или вводишь число не из диапазона, или не число, или даже отправляешь пустоту -- число попыток уменьшается на одну, всего их {attempts}.\nУдачи!\n\nИтак, компьютер загадал число. ")
# print(f"Компьютер загадал число: {random_number}")


while attempts > 0:
    user_number = input("\n\nВведи свой вариант числа: ")

    try:
        check_number = int(user_number)

        if check_number >= 1 and check_number <= 100:

            if check_number < random_number:
                attempts -= 1
                print(f"\nТвоё число меньше загаданного.\nПопыток осталось всего: {attempts}.")
            elif check_number > random_number:
                attempts -= 1
                print(f"\nТвоё число больше загаданного.\nПопыток осталось всего: {attempts}.")
            else:
                if max_attempts != attempts:
                    print(f"\nЙей! Ты угадал! Это действительно число {user_number}!\nИ на угадывание у тебя ушло вот сколько попыток: {max_attempts-attempts+1}.\n")
                else:
                    print(f"\nВот это да! Ты угадал число {user_number} с первой попытки.\n")
                break

        else:
            attempts -= 1
            print(f"Введи число в диапазоне от 1 до 100.\nПопыток осталось всего: {attempts}.\n")

    except ValueError:
        attempts -= 1
        print(f"\nНо ведь \"{user_number}\" не является целым числом.\nПопыток осталось всего: {attempts}.")

    if attempts == 1:
        print(f"Последняя попытка! Посмотри в {random_number-2} -- {random_number+4}")
    elif attempts == 0:
        print(f"\n\nК сожалению на этом и попытки, и игра закончились.\nИскомое число: {random_number}\n")