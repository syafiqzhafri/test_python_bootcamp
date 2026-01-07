# Question 1
student_records = {
    "student1": {"name": "John", "age": 19, "major": "Computer Science", "grades": [85, 92, 78]},
    "student2": {"name": "Sarah", "age": 20, "major": "Biology", "grades": [90, 88, 95]},
}

# Question 2
student_records["student3"] = {
    "name": "Mike", "age": 18, "major": "Math", "grades": [82, 79, 81]
}

print(student_records)

# Question 3
student_records["student1"]["age"] = 20

print(student_records)

# Question 4
for student_id, details in student_records.items():
    name = details["name"]
    major = details["major"]
    print(f"Student ID: {student_id}, Name: {name}, Major: {major}")
