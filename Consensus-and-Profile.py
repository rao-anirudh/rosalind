def dataset(string):
    data = string.split(">")
    return [item[13::] for item in data][1::]  # Assuming FASTA code is Rosalind_XXXX


def profiler(dna_list):
    consensus = ""
    a = "A: "
    c = "C: "
    g = "G: "
    t = "T: "
    profile = []
    for num in range(len(dna_list[0])):
        base_list = ""
        for dna_string in dna_list:
            base_list += dna_string[num]
        profile.append(base_list)

    for item in profile:
        a += f"{item.count('A')} "
        c += f"{item.count('C')} "
        g += f"{item.count('G')} "
        t += f"{item.count('T')} "
        base_count = [item.count('A'), item.count('C'), item.count('G'), item.count('T')]

        for base in ["A", "C", "G", "T"]:
            if item.count(base) == max(base_count):
                consensus += f"{base}"
                break

    return consensus, [a, c, g, t]


with open("C:\\Users\\Anirudh\\Desktop\\rosalind_cons.txt", mode="r") as f:
    content = f.read().replace("\n", "")
    dna = dataset(content)
    f.close()

print("")
con_string, dna_profile = profiler(dna)
print(con_string)
for numbers in dna_profile:
    print(numbers)
