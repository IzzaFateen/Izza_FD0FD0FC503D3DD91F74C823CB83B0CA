class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
# Create a list of student objects
students = [
    Student("Max", "S001", 3.8),
    Student("Tom", "S002", 3.5),
    Student("Ken", "S003", 4.0),
    Student("Izza", "S004", 4.7)
]

# Sort the list of students based on CGPA
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")