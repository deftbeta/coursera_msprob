def extend(perm, n):
  if len(perm) == n:
    print(perm)
    exit()

  for k in range (n):
    if k not in perm:
      perm.append(k)

      if can_be_extended_to_solution(perm):
          extend(perm, n)

          perm.pop()

extend(perm = [], n = 20)
