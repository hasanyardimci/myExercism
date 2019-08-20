cp_dict= {'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine',
          'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
          'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan', 'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'}

def rna_split(RNA):
    i = 0
    rna_seri = ""
    while i < len(RNA):
        rna_seri += RNA[i:i+3] + " "
        i += 3
    return rna_seri.split()

def proteins(strand):
    rna = rna_split(strand)
    protein = ""
    for i in rna:
        if i == 'UAA' or i == 'UAG' or i == 'UGA':
            break
        else:
            protein += cp_dict[i] + " "
    return protein.split()