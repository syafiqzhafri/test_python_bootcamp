student = {
    "name": "Alice",
    "age": 21,
    "grade": "A",
    "courses": ["Math", "Science", "Art"]
}

# Accessing and modifying
print(student["name"])  # Output: Alice
print(student.get("age"))  # Output: 21
student["age"] = 22
student["email"] = "alice@example.com"
print(student.get("age"))

keys = student.keys()
values = student.values()
items = student.items()

print(keys)
print(values)
print(items)

# Iterating through the dictionary

for key in student:
    print(f"{key}: {student[key]}")

for key, value in student.items():
    print(f"{key}: {value}")

# Nested dictionary

company = {
    "employees": {
        "john": {"age": 30, "department": "HR"},
        "jane": {"age": 25, "department": "Finance"}
    },
    "departments": ["HR", "Finance", "IT"]
}

print(company["employees"].items())
print(company["departments"])
