def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

sample_number = 5
print(f"The factorial of {sample_number} is: {factorial(sample_number)}")