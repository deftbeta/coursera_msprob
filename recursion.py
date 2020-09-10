# T(n) is the number of games in a tournament with n teams
# There are two types of games:
    # games that involve the first team: n-1
    # games that don't involve it: T(n-1)

# hence, T(n) = (n-1) + T(T-1)

# each game is counted twice: the game between teams i and j counted as ij and ji
# Thus the total number of games is n(n-1)/2




def T(n):
    if n<= 1:
        return 0
    return (n-1)+T(n-1)
print (T(4))
