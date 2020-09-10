# Rule of product
# If there are n objects of the first type
# and there are k objects of the second type
# then there are n x k pairs of objects of the
# first type and the second type


from itertools import product
a = ['a', 'b']
b = [1,2,3]
print(list(product(a,b)))
