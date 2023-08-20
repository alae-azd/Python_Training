# Unit Conversion Tool

This Python program serves as a simple unit conversion tool that allows you to convert measurements between inches and centimeters. You can choose the type of conversion and input the value you want to convert. The program then provides the converted result based on your selection.

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
4. Choose the type of conversion: inches to centimeters (1) or centimeters to inches (2).
5. Enter the value you want to convert.
6. The program will display the converted result.

## Functions
- `ask_question()`: Prompts the user to choose the type of conversion (inches to cm or cm to inches).
  - Returns `1` for inches to cm conversion or `2` for cm to inches conversion.
- `convert_inches_to_cm()`: Converts inches to centimeters based on user input.
  - Returns the converted value in centimeters.
- `convert_cm_to_inches()`: Converts centimeters to inches based on user input.
  - Returns the converted value in inches.

## Program Logic
1. The program starts by asking the user to choose the conversion type using the `ask_question()` function.
2. Depending on the choice, the program proceeds with the corresponding conversion using either `convert_inches_to_cm()` or `convert_cm_to_inches()`.
3. The converted result is displayed to the user.

## Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

Feel free to modify this README to align with your project's specifics. Enjoy using and customizing the Unit Conversion Tool in `main.py`!
