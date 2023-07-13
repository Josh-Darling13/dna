"""
When I said a really simple function, I meant REALLY simple.
    """

def dna_to_rna(dnaCode):
    to_re = dnaCode.upper()
    return to_re.replace("T","U")

print(dna_to_rna("gactttagcttcgatgatcgatgtgtcagagtgtcagaa"))

