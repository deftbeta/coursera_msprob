# n over k is "n choose k"
# the number of ways of selecting a set (team) of size k
# out of n elements (students)

# n over n-k
# the number of ways to select a set of size n - k
# out of n elements
# this is just the number of ways of partitioning n elements
# into two sets of size n-k

c = dict() # c([n,k]) is equal to "n choose k"

for n in range(8):
    c[n,0] = 1
    c[n,n] = 1

    for k in range(1,n):
        c[n,k] = c[n-1, k-1]+c[n-1,k]

print(c[7,4])
