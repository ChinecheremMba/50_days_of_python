# A function that checks the number of students presence in school. 

def register_check(student_dict):
    students_in_school = 0
    presence_dict = {}  # Dictionary to store the presence status of each student

    for student, status in student_dict.items():
        if status.lower() == "yes":
            students_in_school += 1
            presence_dict[student] = "yes"
        else:
            presence_dict[student] = "no"

    return students_in_school, presence_dict

# Example usage:
student_status = {
    "Alice": "Yes",
    "Bob": "No",
    "Charlie": "Yes",
    "David": "Yes",
    "Eve": "No"
}

total_students, presence_info = register_check(student_status)

print("Total students in school:", total_students)
print("Presence information:")
for student, presence in presence_info.items():
    print(f"{student}: {presence}")
