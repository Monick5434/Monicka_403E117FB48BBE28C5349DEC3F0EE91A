class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with sample student data
students = [
    Student("John Doe", "A123", 3.8),
    Student("Jane Smith", "B456", 3.9),
    Student("Alice Johnson", "C789", 3.7)
]

sorted_students = sort_students(students)

# Print sorted student list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")