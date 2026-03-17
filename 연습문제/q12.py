import numpy as np 
import scipy as sp
from scipy import stats

# 이항 검정
## 1) seed 설정 seed = 0
np.random.seed(0)
## 2) 샘플 추출
random_ber = stats.bernoulli(0.5).rvs(10)
print(random_ber)

n_ber = random_ber.sum()
print(n_ber)

## 3) 가설 검정
binom_test = stats.binomtest(n_ber, n=10, p=0.5)
print(binom_test)