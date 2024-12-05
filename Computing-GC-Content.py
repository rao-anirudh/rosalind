gc = {}


def dataset(string):
    data = string.split(">")
    return data[1::]


def gc_content(string):
    g = string[13::].count("G")  # Assuming FASTA code is Rosalind_XXXX
    c = string[13::].count("C")
    g_c = 100 * (g + c) / len(string[13::])
    gc[string[:13:]] = g_c


with open("C:\\Users\\Anirudh\\Desktop\\rosalind_gc.txt", mode="r") as f:
    content = f.read().replace("\n", "")
    fasta = dataset(content)
    f.close()

for item in fasta:
    gc_content(item)

for tag, value in gc.items():
    if value == max(gc.values()):
        print(tag)
        print(value)
