def multiply_nums(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

if __name__ == "__main__":
    entered_numbers = input("Enter numbers to be multiplied, separated by spaces: ").split()
    if not entered_numbers:
        print("Please enter at least one number.")
    else:
        try:
            numbers = [float(number) for number in entered_numbers]
            print("Answer:", multiply_nums(*numbers))
        except ValueError:
            print("Please enter valid numbers separated by spaces.")
