# Personal Information Analyzer

This Python program is designed to collect and categorize personal information including name, age, and height. It then provides insightful categorizations based on the collected data.

## Prerequisites
- Python 3.x

## Getting Started
1. Ensure Python is installed on your system.
2. Clone or download this repository to your local machine.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing the code.
3. Run the program using the command:
   ```shell
   python main.py
   ```
4. Follow the on-screen prompts to enter your name, age, and height.
5. The program will display your information and provide relevant age and height-based categorizations.

## Functions
- `ask_name()`: Prompts the user to input their name, ensuring it's not empty.
- `ask_age(person_name)`: Asks the user, addressing them by name, to input their age, validating it's a number.
- `ask_height(person_name)`: Asks the user, addressing them by name, to input their height, validating it's a realistic number.
- `display_results(person_name, person_age, person_height)`: Displays the collected data and provides age-related categorizations.

## Program Flow
1. The program starts by collecting the user's name using `ask_name()`.
2. User's age is collected using `ask_age()`.
3. User's height is collected using `ask_height()`.
4. The program displays the collected information and provides age and height categorizations using `display_results()`.

## Age Categories
- Infants (ages 1 or 2)
- Children (ages under 10)
- Teenagers (ages 12 to 17)
- Adults (ages 18 and above)
- Seniors (ages over 60)
- Minors (ages not covered by above categories)

## Contributing
We welcome contributions! If you encounter issues or have suggestions for improvements, please open an issue or pull request.

Feel free to modify this README to suit your project's unique details. Have fun exploring and customizing the Personal Information Analyzer program in `main.py`!
