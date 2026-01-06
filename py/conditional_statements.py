# If Else

while True:
    age_input = input("Please enter your age: ")
    try:
        age = int(age_input)
        if age < 0:
            print("Age cannot be negative. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# And Or

user_age = 18
has_license = True

if user_age >= 18 and has_license:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

weather = "sunny"
temperature = 35

if weather == "sunny":
    if temperature > 30:
        print("It's a hot sunny day.")
    else:
        print("It's a not so sunny la day.")
