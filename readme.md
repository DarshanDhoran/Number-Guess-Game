# Number Guessing Game

This is a simple Python script for a number guessing game. The game generates a random number between 1 and 10, and the user has to guess the number. The user can also quit the game at any time by pressing 'Q'.

## How It Works

1. **Import Module**: The script imports the `random` module to generate a random number.

2. **Generate Target Number**: 
    - `random.randint(1, 10)` generates a random integer between 1 and 10 (inclusive).
    - This number is stored in the variable `target`.

3. **Game Loop**:
    - The script enters a `while True` loop, which runs indefinitely until broken by a condition.
    - The user is prompted to guess the number or quit by pressing 'Q'.
    - If the user enters 'Q', the game breaks out of the loop and ends.
    - The user's input is converted to an integer for comparison with the target number.
    - If the user's guess matches the target number, a success message is displayed, and the loop is broken.
    - If the guess is smaller or larger than the target, appropriate hints are provided.

4. **Game Over**: Once the loop ends, a "Game Over" message is printed.

## Usage

1. **Run the Script**: To play the game, run the script using a Python interpreter.


python number_guessing_game.py


2. **Play**: Enter your guess when prompted. If you wish to quit the game, press 'Q'.

## Example Output

```
Guess the Number or Quit(press Q): 5
Number is Small...
Guess the Number or Quit(press Q): 8
Number is Big...
Guess the Number or Quit(press Q): 7
Success: Correct Guess!
-----Game Over-----
```

## Contributing

If you have suggestions for improvements, feel free to submit a pull request or open an issue.

---

Enjoy playing the Number Guessing Game!