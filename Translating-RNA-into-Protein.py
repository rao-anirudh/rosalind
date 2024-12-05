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


def start_check(rna_string):
    i = 0
    for base in rna_string:
        if rna_string[i:i+3:] == "AUG":
            return rna_string[i::]
        i += 1
    print("\nERROR: No start codon found in sequence")
    return rna_string


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
    print("\nERROR: No stop codon found in sequence")
    return aa_string


rna = input("\nEnter RNA sequence to translate: ").upper()
if "T" in rna:
    rna = rna.replace("T", "U")
    print("\nDNA sequence converted to RNA sequence\n")
rna_start = start_check(rna)
rna_to_translate = triplet_check(rna_start)
rna_codon_split = codon_split(rna_to_translate)
crude_aa_string = raw_translate(rna_codon_split)
final_aa_string = stop_check(crude_aa_string)

print(f"\nLength of sequence provided: {len(rna)}")
print(f"Length of sequence translated: {len(final_aa_string)*3}")
print(f"Translation started at base number {rna.index(rna_to_translate)+1}")
print(f"Translation stopped at base number {rna.index(rna_to_translate)+(len(final_aa_string)*3)}")
print(f"Sequence translated: {rna_to_translate}")

print(f"\nTranslated amino acid sequence:\n{final_aa_string}")

