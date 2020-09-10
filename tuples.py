# Tuples
# The number of sequences of length k
#composed of n symbols is n^k


from itertools  import product

for p in product ("ab", repeat = 4):
    print("".join(p))
