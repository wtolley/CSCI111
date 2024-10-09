# List of student records: (Name, ID, GPA)
students = [
    ('Alice', 102, 3.5),
    ('Bob', 104, 3.8),
    ('Charlie', 103, 3.0),
    ('David', 101, 3.9),
    ('Eva', 105, 3.7)
]

# Function to extract the GPA from a student record
def get_gpa(student):
    return student[2]

# 1. Sort the list of students by their GPA in descending order using the custom function
sorted_students = sorted(students, key=get_gpa, reverse=True)
print("Sorted Students by GPA (Descending):", sorted_students)

# 2. Find the student with the highest GPA
top_student = sorted_students[0]
print("Student with the highest GPA:", top_student)

# 3. Unpack each student's name and GPA, and print them
print("Student Records:")
for student in sorted_students:
    name, _, gpa = student  # Unpack, ignoring the ID
    print(f"Student: {name}, GPA: {gpa}")

# 4. Calculate the average GPA
total_gpa = sum(get_gpa(student) for student in students)
average_gpa = total_gpa / len(students)
print(f"Average GPA: {average_gpa:.2f}")
