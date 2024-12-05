def mortal_rabbits(n, m):
    b = [0, 1, 0, 1]                    # number of births
    p = [0, 1, 1, 2]                    # population size
#month   0  1  2  3
    for x in range(4, n+1):             # x = month number
        if x >= m:                      # month number equal to or more than lifespan of first generation
            b.append(p[x - 1] - b[x - 1])
            p.append((2 * b[x]) + b[x - 1] - b[x - m])
        else:                           # month number lesser than lifespan of first generation
            b.append(p[x - 1] - b[x - 1])
            p.append((2 * b[x]) + b[x - 1])
    return p[n]


value = mortal_rabbits(19, 2)
print(value)
