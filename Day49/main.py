def even_or_average():
    numbers = []
    for _ in range(5):
        num = int(input("Enter a number: "))
        numbers.append(num)
    
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    if even_numbers:
        largest_even = max(even_numbers)
        return largest_even
    else:
        average = sum(numbers) / len(numbers)
        return average

result = even_or_average()
print("Result:", result)
