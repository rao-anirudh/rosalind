s = input("Enter DNA string: ")
t = input("Enter DNA substring to find: ")

i = 0
positions = ""
for char in s:
    if s[i:i+len(t):] == t:
        positions += f"{i+1} "
    i += 1

print(positions)
