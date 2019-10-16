from typing import List

def sort_bigrams(sequence: List[str]) -> List[List[str]]:
    empty_list = []
    for x in range(len(sequence)-1):
        empty_list.append((sequence[x], sequence[x+1]))
    return empty_list

tokens = []
assert not sort_bigrams(tokens)

tokens = ["hypomnesia"]
assert not sort_bigrams(tokens)

tokens = ["Stately", "plump", "Buck", "Mulligan", "came", "from", "the", "stairhead", "bearing", "a", "bowl", "of", "lather", "on", "which", "a", "mirror", "and", "a", "razor", "lay", "crossed"]
assert sort_bigrams(tokens)
