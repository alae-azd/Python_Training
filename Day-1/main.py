# DAY #1 Code


def ask_name():  # Ask for name
    name_str = ""
    while name_str == "":
        name_str = input("What is your name? ")
    return name_str


def ask_age(person_name):  # Ask for age
    age_int = 0
    while age_int == 0:
        age_str = input(person_name + ", what is your age? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERROR: Please enter a number for age")
    return age_int


def ask_height(person_name):
    height_float = 0
    while height_float == 0:
        height_str = input(person_name + ", what is your height? ")
        try:
            height_float = float(height_str)
        except ValueError:
            print("ERROR: Please enter a number for height")
        else:
            if height_float > 2.5:
                print("Please enter a realistic height in meters")
                height_float = 0
    return height_float


def display_results(person_name, person_age, person_height):
    print()
    print("Your name is " + person_name + ", you are " + str(person_age) + " years old.")
    print("Next year, you will be " + str(person_age + 1) + " years old.")

    if person_age == 17:
        print("You are almost an adult.")
    elif person_age == 18:
        print("Just turned adult: Congratulations!")
    elif person_age == 1 or person_age == 2:
        print("You are a baby.")
    elif 12 <= person_age < 18:
        print("You are a teenager.")
    elif person_age > 60:
        print("You are a senior.")
    elif person_age < 10:
        print("You are a child.")
    elif person_age > 18:
        print("You are an adult.")
    else:
        print("You are a minor.")

    # Display height
    print("Your height: " + str(person_height) + " m")

# ------------------------------------------------------------------------------------------------

name = ask_name()
age = ask_age(name)
height = ask_height(name)
display_results(name, age, height)
