# # Create a multiplication table for numbers 1 through 10

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print()  # Print a blank line after each table for better readability

# Write a program that finds all prime numbers up to a given number.(limit = 20)
limit = 20
primes = []
for num in range(2, limit + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(primes)
