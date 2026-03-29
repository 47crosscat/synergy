import random

random_number = random.randint(1,100)

# print(f"Случайное число: {random_number}")
print(f"\nДобрый день!\n\nДавайте сыграем в игру \"Угадай число\".\nЧисло выбрано случайным образом в диапазоне от 1 до 100.")
user_number = input("\nВведите свой вариант числа: ")

check_number = int(user_number)

if check_number < random_number:
    print(f"Ваше число меньше загаданного.")
elif check_number > random_number:
    print(f"Ваше число больше загаданного.")
else:
    print(f"Вы угадали!")
