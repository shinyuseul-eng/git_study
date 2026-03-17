from itertools import product
from itertools import combinations_with_replacement
students = ['A','B','C','D','E','F']

# 중복조합

re_com = list(combinations_with_replacement(students,2))
re_com_num = len(re_com)

print(re_com)
print(re_com_num)