def multiplication_table(number):
    multiplier = 1  # Initialize the appropriate variable

    while multiplier <= 5:  # Complete the while loop condition.
        result = number * multiplier
        if result > 25:
            print("Result is greater than 25")  # Enter the action to take if the result is greater than 25
        else:
            print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        multiplier += 1  # Increment the appropriate variable

multiplication_table(3)
#should print 
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

multiplication_table(5)
# Should print:
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25

multiplication_table(8)
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24




