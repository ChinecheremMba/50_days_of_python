import math

def divide_or_square(number):
    if number % 5 == 0:
        return math.sqrt(number)
    else:
        return number % 5


result1 = divide_or_square(25)  # 25 is divisible by 5, so its square root will be returned
result2 = divide_or_square(7)   # 7 is not divisible by 5, so its remainder when divided by 5 will be returned

print("Result 1:", result1)     # Output: Result 1: 5.0 (square root of 25)
print("Result 2:", result2)     # Output: Result 2: 2 (remainder of 7 divided by 5)
