# For Loop

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)

# While Loop

count = 0
while count < 5:
    print(count)
    count += 1

# Loop Control Statements

for i in range(10):
    if i == 3:
        continue        # Skip this iteration
    if i == 7:
        break           # Exit the loop
    print(i)

# Nested Loops

for i in range(2):
    for j in range(3):
        print(f"({i},{j})")
