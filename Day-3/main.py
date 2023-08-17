import random

def ask_number(min_num, max_num):
    int_number = 0
    while int_number == 0:
        str_number = input(f"What is the magic number (between {min_num} and {max_num}): ")
        try:
            int_number = int(str_number)
        except ValueError:
            print("ERROR: You should enter a number.")
        else:
            if int_number > max_num or int_number < min_num:
                print(f"Please enter a number between {min_num} and {max_num}.")
                int_number = 0
    return int_number

MIN_NUMBER = 1
MAX_NUMBER = 10
LIVES_COUNT = 4
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)

number = 0
while not number == MAGIC_NUMBER and LIVES_COUNT > 0:
    print(f"You have {LIVES_COUNT} lives remaining.")
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    if number > MAGIC_NUMBER:
        print("The magic number is smaller.")
        LIVES_COUNT -= 1
    elif number < MAGIC_NUMBER:
        print("The magic number is larger.")
        LIVES_COUNT -= 1
    else:
        print("Congratulations, you have won!")
        break

if LIVES_COUNT == 0:
    print(f"You have lost! The magic number was: {MAGIC_NUMBER}")
