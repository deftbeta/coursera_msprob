# k- permutations
# The number of sequences of length k with no
# repetitions composed out of n symbols is
# n(n-1) .... (n-k+1) = n! / (n-k)!


from itertools import permutations
for p in permutations ("0123456789", 5):
        print("".join(p))
