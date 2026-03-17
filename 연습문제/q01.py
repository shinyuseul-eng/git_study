# ! 함수 정의 
def fac(n):
    result = 1
    for i in range(1, n +1):
        result = result * i
    return result
    
# 4! 계산
print(fac(4))