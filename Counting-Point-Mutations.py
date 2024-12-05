def hamming(s, t):
    d_h = 0
    for index in range(len(s)):
        if s[index] != t[index]:
            d_h += 1

    return d_h


seq1 = input("Enter Seq 1: ")
seq2 = input("Enter Seq 2: ")
hamming_dist = hamming(seq1, seq2)
print(hamming_dist)
