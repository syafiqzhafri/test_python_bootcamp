fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]
empty_list = []

# Accessing elements
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry
print(numbers[1:4])  # Output: [2, 3, 4]

fruits.append("grape")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'grape']
fruits.insert(2, "orange")
print(fruits)  # Output: ['apple', 'banana', 'orange', 'cherry', 'grape']
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']
popped = fruits.pop()
print(popped)  # Output: grape
fruits.sort()
print(fruits)  # Output: ['apple', 'cherry', 'orange']
fruits.reverse()
print(fruits)  # Output: ['orange', 'cherry', 'apple']

len(fruits)  # Output: 3
print(len(fruits))
"apple" in fruits  # Output: True
print("apple" in fruits)
fruits + ["mango"]  # Output: ['orange', 'cherry', 'apple', 'mango']
print(fruits + ["mango"])
# Output: ['orange', 'cherry', 'apple', 'orange', 'cherry', 'apple']
fruits * 2
print(fruits * 2)
print(len(fruits))  # Output: 3
