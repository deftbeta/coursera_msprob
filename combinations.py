# The number of games in a tournament with n teams
# (each pair of teams played eachother exactly once)
# is n(n-1)/2


from itertools import combinations

for c in combinations ("0123456789",5):
    print("".join(c))
