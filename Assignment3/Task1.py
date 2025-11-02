# Task: Calculate Factorial Using a Function
# Author: Annapurna Sahu

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number to find its factorial: "))
print("Factorial of", num, "is:", factorial(num))
