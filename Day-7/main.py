import os
import time
import random

# Function to clear the screen based on the operating system
def clear_screen():
    if os.name == 'posix':
        os.system('clear')  # Clear screen on Unix-based systems
    else:
        os.system('cls')    # Clear screen on Windows systems

sequence = ""
for i in range(3):
    number = random.randint(1, 9)
    sequence += str(number)  # Generate a random number and add it to the sequence

clear_screen()
print("Welcome to the Simon game")

score = 0
while True:
    print("Remember the sequence")
    time.sleep(1)
    print(sequence)  # Display the sequence for the player to remember
    time.sleep(3)
    clear_screen()
    response = input("Your answer: ")  # Get the player's input sequence
    time.sleep(1)
    clear_screen()
    if response == sequence:
        score += 1
        number = random.randint(0, 9)
        sequence += str(number)  # If the player's input matches the sequence, add a new random number to the sequence
        print(f"Correct answer, your score is {score}")
        time.sleep(1)
        clear_screen()
    else:
        print("Wrong answer")
        print(f"The sequence was {sequence}")  # If the player's input is wrong, display the correct sequence
        print(f"Your final score is: {score}")  # Display the final score
        break  # Exit the game loop
