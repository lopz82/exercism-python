TRANSCRIBED = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}


def to_rna(dna_strand: str) -> str:
    return "".join(TRANSCRIBED.get(dna, "") for dna in dna_strand)
