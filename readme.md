Random Password Generator

This is a simple Python script that generates a random password of a specified length. The generated password contains a mix of uppercase and lowercase letters, digits, and punctuation characters.

How It Works

Import Modules: The script imports the random and string modules. 
    - `random`: This module implements pseudo-random number generators for various distributions.
    - `string`: This module contains a collection of string constants which include ASCII letters, digits, and punctuation.

2Password Length: The variable `pass_len` is set to `12`, meaning the generated password will be 12 characters long. You can change this value to generate passwords of different lengths.

3.Character Set: The variable `charValues` combines:
    - `string.ascii_letters`: All lowercase and uppercase letters.
    - `string.digits`: All decimal digit characters.
    - `string.punctuation`: All printable ASCII punctuation characters.

4.Password Generation: 
    - An empty string `password` is initialized.
    - A for-loop runs `pass_len` times, and during each iteration, a random character from `charValues` is appended to the `password`.

5.Output: The generated password is printed to the console.


    1.Run the Script: To generate a random password, simply run the script using a Python interpreter.

    python random_password_generator.py


    2.Customize: If you need a password of a different length, change the value of `pass_len`.

    3.Security Note: While this script can generate random passwords, for high-security applications, consider using more robust libraries      such as secrets which is designed for cryptographic purposes.

Example Output

Your Password is : &Ww5B@3m^zA%

Contributing

If you have suggestions for improvements, feel free to submit a pull request or open an issue.


Enjoy using the Random Password Generator! Stay secure.