import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats


# Q1. 이항분포pmf 그리기 
# 이항분포 생성
n, p = 10, 0.5
stat_bin = stats.binom(n, p)

# 그리기
fig, ax = plt.subplots()
## pmf를 만드는 코드를 작성해 주세요
x_axis = np.arange(n + 1) 
ax.bar(x_axis, stat_bin.pmf(x_axis))


##
plt.show()
fig.savefig("pmf_plot.png")


# Q2. 이항분포cdf 그리기 
## cdf 만드는 코드를 작성해 주세요
x_axis = np.arange(n + 1) 
plt.bar(x_axis, stat_bin.cdf(x_axis))
plt.show()


##
plt.show()
fig.savefig("cdf_plot.png")



# Q3. 랜덤표본 추출
## seed 설정 seed = 0 
np.random.seed(0)

## 랜덤 샘플 추출
random_bin = stat_bin.rvs(100)
## 평균계산
bin_mean = random_bin.mean()
