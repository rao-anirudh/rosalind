def dataset(string):
    data = string.split(">")
    return [item[13::] for item in data][1::]  # Assuming FASTA code is Rosalind_XXXX


def splice(string_list):
    for substring in string_list[1::]:
        if substring in string_list[0]:
            string_list[0] = string_list[0].replace(substring, "")
    return string_list[0]


rna_codon_table = open("RNA Codon Table.txt", mode="r")
rna_codons = rna_codon_table.read().replace(' ', '').split("\n")
codon_lookup = {}
for codon in rna_codons:
    codon_lookup[codon[0:3:]] = codon[3::]


def triplet_check(rna_string):
    if len(rna_string) % 3 == 0:
        return rna_string
    elif len(rna_string) % 3 == 1:
        return rna_string[:len(rna_string)-1:]
    elif len(rna_string) % 3 == 2:
        return rna_string[:len(rna_string)-2:]


def codon_split(rna_string):
    n = 3
    codons = [rna_string[i:i+n] for i in range(0, len(rna_string), n)]
    return codons


def raw_translate(codon_list):
    return "".join([codon_lookup[item] for item in codon_list])


def stop_check(aa_string):
    i = 0
    for aa in aa_string:
        if aa_string[i:i+4:] == "Stop":
            return aa_string[:i:]
        i += 1


with open("C:\\Users\\anira\\Desktop\\rosalind_splc.txt", mode="r") as f:
    content = f.read().replace("\n", "")
    dna = dataset(content)
    f.close()

spliced_dna = splice(dna)
spliced_rna = triplet_check(spliced_dna.replace("T", "U"))
spliced_rna_codons = codon_split(spliced_rna)
amino_acids = raw_translate(spliced_rna_codons)
final_aa = stop_check(amino_acids)
print(final_aa)
