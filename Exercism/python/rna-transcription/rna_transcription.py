def to_rna(dna_strand):
    dic = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    a = ''.join([dic[x] for x in dna_strand])
    return a
