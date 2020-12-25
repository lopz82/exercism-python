from typing import List

PROTEINS = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
}


def proteins(strand: str) -> List[str]:
    codons = (strand[i:i + 3] for i in range(0, len(strand), 3))
    sequence = []
    for codon in codons:
        res = PROTEINS.get(codon, None)
        if not res:
            break
        sequence.append(res)
    return sequence
