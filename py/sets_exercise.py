# Create a system that stores student grades as tuples (name, subject, grade) and uses sets to find unique subjects and students.

grades = [
    ("Alice", "Math", 90),
    ("Bob", "Math", 85),
    ("Alice", "Science", 95),
    ("Bob", "History", 88),
    ("Charlie", "Math", 92),
    ("Charlie", "Science", 89),
    ("Alice", "History", 91),
]

# Find all unique students
students = set()
for grade in grades:
    students.add(grade[0])
print("Unique Students:", students)

# Find all unique subjects
subjects = set()
for grade in grades:
    subjects.add(grade[1])
print("Unique Subjects:", subjects)

# Find Alice grade
alice_grades = []
for grade in grades:
    if grade[0] == "Alice":
        alice_grades.append((grade[1], grade[2]))
print("Alice's Grades:", alice_grades)
