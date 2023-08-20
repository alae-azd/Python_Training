def ask_question():
    print("Conversion:")
    print("1 - inches => cm")
    print("2 - cm     => inches")
    choice_str = ""
    while choice_str == "":
        choice_str = input("Please choose the type of your conversion (1 or 2): ")
        try:
            choice_int = int(choice_str)
        except ValueError:
            print("ERROR: You must enter a number")
            choice_str = "" 
        else:
            if not choice_int == 1 and not choice_int == 2:
                print("You must choose either 1 or 2")
                choice_str = ""
    return choice_int


def convert_inches_to_cm():
    inches_value_str = ""
    while inches_value_str == "":
        inches_value_str = input("Please enter the value to convert to 'cm': ")
        try:
            inches_value_int = int(inches_value_str)
        except ValueError:
            print("ERROR: You must enter a number")
            inches_value_str = ""
        else:
            cm_value_int = inches_value_int * (254 / 100)
    return cm_value_int


def convert_cm_to_inches():
    cm_value_str = ""
    while cm_value_str == "":
        cm_value_str = input("Please enter the value to convert to 'inches': ")
        try:
            cm_value_int = int(cm_value_str)
        except ValueError:
            print("ERROR: You must enter a number")
            cm_value_str = ""
        else:
            inches_value_int = cm_value_int * (394 / 1000)
    return inches_value_int 


def main():
    choice = ask_question()
    if choice == 1:
        cm_value = convert_inches_to_cm()
        print(f"Result: {cm_value} cm")
    else:
        inches_value = convert_cm_to_inches()
        print(f"Result: {inches_value} inches")


if __name__ == "__main__":
    main()
