# 오류의 종류
# 1종의 오류(a) : 귀무가설이 참일 때 귀무가설을 기각하는 경우
# 2종의 오류(b) : 귀무가설이 거짓일 때 귀무가설을 채택하는 경우
# 실제:참:옳은결정(Ho채택):잘못된결정(1종의오류)
# 실제:거짓:잘못된결정:옳은결정
# <오류의종류 >*가설검정은 표본자료만으로 모집단에 대한 가설을 검토하므로 오류 존재
# 바람직한 가설은 두 오류를 최소화하는 것
# 전통적인 통계학에서의 검정->1종의 오류를 범할 확률을 최소화
# <가설 검정 과정> 가설설정-> 표본자료의 관측->가설검정에 사용할 통계량
# <감정 통계량>
# 기각역:x_bar
import matplotlib.pyplot as plt
plt.bar(['seoul','paris','seattle'],[20,30,40])
plt.xlabel('ciry')
plt.ylabel('response')
plt.title("experiment result")
# pit.scatter([1,2,3,],[4,5,6], s=20, c='g',marker='x', cmap='Blues')
plt.show()
# cmap
# hist() vs bar()
# 연속형    범주형
# 구간분할  카테고리
# 후 빈도수
# subplot(nrow,ncols,index)
# import matplotlib.pyplot as plt
import numpy as np
x= np.random.rand(5)
y= np.random.rand(5)
plt.subplot(2,2,1)
plt.scatter(x, y, s=80, c='r', marker='>')
plt.subplot(222)
plt.scatter(x, y, s=80, c='b', marker=(5,0))
plt.subplot(223)
plt.scatter(x, y, s=80, c='g', marker='*')
plt.subplot(224)
plt.scatter(x, y, s=80, c='k', marker='v')
plt.show()

fig, axes= plt.subplots(2,2)
print(type(axes))
axes[0,0].scatter(x,y, s=80, c='r', marker='>')
axes[0,1] .scatter(x,y, s=80, c='g', marker='*' )
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
df = sns. load_dataset('tips')
print(df.head())
sns.jointplot(x='total_bill', y='tip', data=df, kind='reg')
plt.show()
