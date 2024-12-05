transitions = {"A": "G", "G": "A", "C": "T", "T": "C"}


def fasta_remover(dataset):
    data = dataset.split(">")
    return [item[13::] for item in data][1::]  # Assuming FASTA is Rosalind_XXXX


def mutations(data):
    dna1 = data[0]
    dna2 = data[1]

    transition = 0
    transversion = 0

    for i in range(0, len(dna1)):
        if dna1[i] == dna2[i]:
            continue
        if transitions[dna1[i]] == dna2[i]:
            transition += 1
            continue
        transversion += 1

    return transition / transversion


with open("C:\\Users\\anira\\Desktop\\rosalind_tran.txt", mode="r") as f:
    content = f.read().replace("\n", "")
    ratio = mutations(fasta_remover(content))
    print(f"{ratio:.11f}")
    f.close()
