# Exercise 1: Create a simple calculator that takes two number and an operation from user.

score_1 = input("Enter first score: ")
score_2 = input("Enter second score: ")

# Input Validation
while True:
    try:
        score_1 = float(score_1)
        score_2 = float(score_2)
        break
    except ValueError:
        print("Please enter valid numbers for scores.")
        score_1 = input("Enter first score: ")
        score_2 = input("Enter second score: ")

# Output Validation
print(f"Your total score is {score_1 + score_2}")

# Exercise 2: Create a simple quiz program with 3 questions. At the end of the quiz, display the total score.

q1 = input("What is the capital of Uganda? ")
q2 = input("What is 26 + 0.1? ")
q3 = input("What is the chemical symbol for gold? ")

# Input Validation
while True:
    try:
        score = 0

        if q1.strip().lower() == "kampala":
            score += 1
        if abs(float(q2) - 26.1) < 0.01:
            score += 1
        if q3.strip().lower() == "au":
            score += 1

        break
    except ValueError:
        print("Please answer all questions correctly.")

# Output Validation
print(f"Your total quiz score is {score} out of 3")
if score == 3:
    print("Excellent work!")
elif score < 2:
    print("Noob")
