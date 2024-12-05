def exp_dom(couples):
    genotypes = couples.split()
    o1 = int(genotypes[0]) * 1
    o2 = int(genotypes[1]) * 1
    o3 = int(genotypes[2]) * 1
    o4 = int(genotypes[3]) * 0.75
    o5 = int(genotypes[4]) * 0.5
    o6 = int(genotypes[5]) * 0
    return 2*(o1+o2+o3+o4+o5+o6)


couple_no = input("\nEnter number of couples in correct genotype order: ")
result = exp_dom(couple_no)
print(result)
