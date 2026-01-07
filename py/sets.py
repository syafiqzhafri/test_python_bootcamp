fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# Set Operations

fruits.add("grape")     # Add element
fruits.remove("banana")  # Remove element
fruits.discard("kiwi")  # No error if not present

print(fruits)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))          # Union
print(set1.intersection(set2))   # Intersection
print(set1.difference(set2))     # Difference
