def is_even(p):
  parity = 1
  for i in (range(len(p)-1)):
    if p[i] != i:
      parity *=-1
      mn = min(range(i, len(p)))
      q=p.index(mn)
      p[i],p[q]=p[q],p[i]
  if parity == 1:
        return True
  else:
        return False

z = is_even([0,3,2,4,5,6,7,1,9,8,10])
print(z)
#is_even([0,3,2,4,5,6,7,1,9,8])
