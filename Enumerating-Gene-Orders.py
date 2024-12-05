from itertools import permutations
from math import factorial

n = int(input("n = "))

if n <= 9:
    fact = factorial(n)
    print(fact)
    n_string = ""
    for num in range(1, n + 1):
        n_string += str(num)
    perms = [" ".join(p) for p in permutations(n_string)]
    for perm in perms:
        print(perm)
else:
    print("ERROR: n is too large to list permutations for")
