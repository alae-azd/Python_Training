# Egg Cooking Timer

This Python program simulates an egg cooking timer, allowing you to choose the desired egg doneness and monitor the cooking process. You can select from soft-boiled, medium-boiled, or hard-boiled eggs, and the program will provide real-time feedback on the cooking progress.

## Prerequisites
- Python 3.x

## Getting Started
1. Ensure Python is installed on your system.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing the code.
3. Run the program using the command:
   ```shell
   python main.py
   ```
4. Choose the desired egg doneness by entering `1`, `2`, or `3`.
5. The program will display real-time progress dots during the cooking process.
6. Once the cooking time is reached, the program will display a "Cooking finished" message.

## Functions
- `choose_doneness()`: Displays the available egg doneness options and prompts the user to choose.
  - Returns `1`, `2`, or `3` based on user input.
- `calculate_duration(choice)`: Calculates the corresponding cooking duration in seconds based on the chosen doneness.
  - Returns the cooking duration in seconds.
- `display_progress(duration)`: Initiates a countdown loop, displaying progress dots and time remaining.
- `main()`: The main program logic that orchestrates the egg cooking timer process.

## Program Logic
1. The program starts by asking the user to choose the desired egg doneness using the `choose_doneness()` function.
2. Based on the user's choice, the program calculates the cooking duration in seconds using the `calculate_duration()` function.
3. The `display_progress()` function is called, initiating a countdown loop that displays progress dots and time remaining.
4. Once the cooking time is reached, the program displays a "Cooking finished" message.

## Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

Feel free to modify this README to suit your project's specific details. Enjoy using and customizing the Egg Cooking Timer in `main.py`!
