from itertools import permutations 
from itertools import combinations
students = ['A','B','C','D','E','F']
# 조합 : 6명 수강생 중 2명에게 순위 상관없이 상품을 주는 경우의 수 
rank_com = list(combinations(students, 2))
rank_com_num = len(rank_com)

print(rank_com)
print(rank_com_num)