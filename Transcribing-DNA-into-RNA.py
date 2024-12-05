def transcriber(dna_string):
    rna_string = dna_string.upper().replace("T", "U")
    return rna_string


bases = input("Enter DNA sequence: ")
print(transcriber(bases))
