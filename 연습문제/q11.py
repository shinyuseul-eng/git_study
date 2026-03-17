import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
# 정규분포
stat_nor = stats.norm(0, 1)

# Q1. 정규분포 pdf 그리기
fig, ax = plt.subplots()
## pdf를 만드는 코드를 작성해 주세요
x_axis = np.linspace(-3, 3, 100)
plt.plot(x_axis, stat_nor.pdf(x_axis))
##
plt.show()
fig.savefig("pdf_plot.png")
# Q2. 정규분포 cdf 그리기 
## cdf 만드는 코드를 작성해 주세요
x_axis = np.linspace(-3, 3, 100)
plt.plot(x_axis, stat_nor.cdf(x_axis))
##
plt.show()
fig.savefig("cdf_plot.png")
# Q3. 정규분포 샘플링
## seed 설정
np.random.seed(0)
## 샘플 추출
random_nor = stat_nor.rvs(100)
print(random_nor) 

## 평균 계산
nor_mean = random_nor.mean()
print(nor_mean)