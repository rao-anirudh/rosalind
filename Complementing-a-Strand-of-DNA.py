def reverse_complement(seq):
    pairs = {"A": "T", "T": "A", "G": "C", "C": "G"}
    rev_seq = seq[::-1].upper()
    rev_comp = ""
    for base in rev_seq:
        rev_comp += pairs[base]
    return rev_comp


bases = input("Enter base sequence: ")
print(reverse_complement(bases))
