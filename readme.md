# Number Multiplier

A small Python command-line program that multiplies any number of values entered by the user.

## Run

From the project directory, start the program with:

```bash
python app.py
```

Enter numbers separated by spaces when prompted. For example:

```text
Enter numbers to be multiplied, separated by spaces: 2 3 4
Answer: 24.0
```

The program accepts integers, decimals, and negative numbers. If the input is empty or contains a non-numeric value, it displays an error message.

## Tests

Run the unit tests from the project directory:

```bash
python -m unittest discover -s test -v
```