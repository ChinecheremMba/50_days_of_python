'''write a code that will count how many males and females are in the list'''

students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

# Convert all elements to lowercase to ensure case-insensitive counting
students = [s.lower() for s in students]

# Initialize counters for male and female students
male_count = students.count('male')
female_count = students.count('female')

# Create a list of tuples
result = [("Male", male_count), ("female", female_count)]

print(result)
