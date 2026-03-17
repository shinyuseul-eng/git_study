import numpy as np 
import scipy as sp
from scipy import stats

# 모평균 가설검정
## 1) seed 설정 seed = 0

## 2) 샘플 추출
random_nor = stats.norm(0,1).rvs(10) 
print(random_nor)

# 평균 계산
nor_mean = random_nor.mean()
print(nor_mean)

## 3) 모평균 가설 검정 함수 정의
def ztest(stat, mu, sigma):
    z = (stat - mu) / (sigma / np. sqrt(10))
    return(z)

## 4) 모평균 가설 검정
mu_test = ztest(nor_mean, 0, 1)
print(mu_test)