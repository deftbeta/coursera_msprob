# this code calculates the number of k combinations
# in a subset of size k of an n element set
# "n choose k"

# (n over k) = n! / k!(n-k)!


n =4
count =0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i<j and j<k:
                count += 1

print(count)
