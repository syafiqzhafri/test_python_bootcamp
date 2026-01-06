BMI = input("Enter your BMI: ")

try:
    bmi_value = float(BMI)

    if bmi_value < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi_value < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi_value < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")
except ValueError:
    print("Invalid input. Please enter a numeric value for BMI.")
