from itertools import product
from itertools import combinations_with_replacement

# 중복순열
students = ['A','B','C','D','E','F']
re_per = list(product(students, repeat=2))
re_per_num = len(re_per)

print(re_per)
print(re_per_num)