prefixes = {}
suffixes = {}
adj_list = []


def dataset(data_string):
    data = data_string.split(">")
    for item in data[1::]:
        fasta = item[:13:]
        pre = item[13:16:]
        suf = item[len(item)-3::]
        prefixes[fasta] = pre
        suffixes[fasta] = suf


# test = ">Rosalind_0498AAATAAA>Rosalind_2391AAATTTT>Rosalind_2323TTTTCCC>Rosalind_0442AAATCCC>Rosalind_5013GGGTGGG"
# dataset(test)

with open("C:\\Users\\anira\\Desktop\\rosalind_grph.txt", mode="r") as f:
    content = f.read().replace("\n", "")
    dataset(content)
    f.close()


for fasta1, suffix in suffixes.items():
    for fasta2, prefix in prefixes.items():
        if suffix == prefix and fasta1 != fasta2:
            edge = f"{fasta1} {fasta2}"
            adj_list.append(edge)

print("")
for entry in adj_list:
    print(entry)
