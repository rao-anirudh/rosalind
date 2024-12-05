def rabbit_pairs(n, k):
    a, b = 0, 1
    for month in range(2, n + 1):
        a, b = b, b+(k*a)
    return b


months = int(input("\nEnter number of months after which total pairs is to be found: "))
pair = int(input("Enter number of pairs produced per mating: "))
result = rabbit_pairs(months, pair)
print(f"\nTotal number of pairs: {result}")
