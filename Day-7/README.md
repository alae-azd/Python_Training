# Simon Memory Game

This Python program simulates the classic Simon Memory Game, where players must remember and replicate a sequence of randomly generated numbers. The game challenges players to test their memory skills and progressively increases the sequence's length as they succeed.

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
4. The game will display a sequence of numbers for you to remember.
5. After a brief moment, the screen will be cleared.
6. Input the sequence you remember and hit Enter.
7. Your answer will be checked. If correct, your score will increase, and the game will continue. If incorrect, the correct sequence and your final score will be displayed.

## Functions
- `clear_screen()`: Clears the terminal screen based on the operating system.
- `generate_sequence()`: Generates a random sequence of numbers for the player to remember.
- `main()`: The main game logic that guides the flow of the Simon Memory Game.

## Program Logic
1. The program generates a random sequence of numbers using the `generate_sequence()` function.
2. The game loop begins, and the player is asked to remember the sequence for a short period.
3. After the sequence is displayed, the screen is cleared.
4. The player inputs their remembered sequence.
5. The player's input is compared to the generated sequence. If correct, the score is increased, a new random number is added to the sequence, and the game continues. If incorrect, the correct sequence and final score are displayed, and the game loop ends.

## Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

Feel free to modify this README to suit your project's specific details. Enjoy playing and customizing the Simon Memory Game in `main.py`!
