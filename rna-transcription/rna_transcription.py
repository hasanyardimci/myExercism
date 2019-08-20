def to_rna(dna_strand):
    dna = "GCTA"
    rna = "CGAU"
    dna2rna = dna_strand.maketrans(dna,rna)
    return dna_strand.translate(dna2rna)
