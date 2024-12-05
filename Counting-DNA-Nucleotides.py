def nucleotide_counter(seq):
    seq = seq.upper()
    return f"{seq.count('A')} {seq.count('C')} {seq.count('G')} {seq.count('T')}"


bases = input("Enter base sequence: ")
print(nucleotide_counter(bases))
