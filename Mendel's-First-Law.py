import math

def nCr(n, r):
    f = math.factorial
    return f(n)/(f(r) * f(n-r))


def prob_dom(k, m, n):
    sample_space = nCr(k+m+n, 2)
    favourable = nCr(k, 2) + (0.75 * nCr(m, 2)) + k*(m+n) + (0.5*m*n)
    return favourable/sample_space


homo_dom = int(input("\nNumber of homozygous dominant individuals: "))
hetero = int(input("Number of heterozygous individuals: "))
homo_rec = int(input("Number of homozygous recessive individuals: "))
print(f"\nProbability of offspring displaying dominant phenotype = {prob_dom(homo_dom, hetero, homo_rec)}")

