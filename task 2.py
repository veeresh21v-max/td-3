import math

def calculate_math_functions():
    try:
        number = float(input("Enter a number: "))
        square_root = math.sqrt(number)
        natural_log = math.log(number)
        sine_value = math.sin(number)
        print(f"The square root of {number} is: {square_root}")
        print(f"The natural logarithm of {number} is: {natural_log}")
        print(f"The sine of {number} is: {sine_value}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

calculate_math_functions()