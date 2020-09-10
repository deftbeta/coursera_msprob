# counting subsets
# You're organizing a car journey.
# you have 5 friends and 3 vacant seats in car
# what is the number of ways to taking 3 of your friends?

# what is the number of ways of choosing n (3) elements out of a set of of size k (5)
# number of combinations = n! /k!(n-k)!

import itertools as it

for c in it.combinations("0123456789",5):
    print("".join(c))
