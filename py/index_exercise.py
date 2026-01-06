# Create a grocery list and perform various operations

list = ["cabbage", "carrot", "celery"]

list.append("broccoli")
list.insert(1, "spinach")
list.remove("carrot")
popped_item = list.pop()
list.sort()
list.reverse()

len(list)
"cabbage" in list
list + ["lettuce"]
list * 2

# Write a program that finds the largest and smallest number in the list.

inputs = []
for i in range(5):
    value = input(f"Enter value {i+1}: ")
    inputs.append(value)

lowest = min(inputs)
print(f"The lowest value is: {lowest}")
highest = max(inputs)
print(f"The highest value is: {highest}")
