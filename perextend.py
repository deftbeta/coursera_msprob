def can_be_extended_to_solution(perm):
  i = len(perm) - 1
  for j in range (i):
    if i - j == abs(perm[i]-perm[j]):
      return False
    return True
