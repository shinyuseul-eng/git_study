import random
answer_Q1andQ2 = 0
answer_Q2 = 0
answer_Q1orQ2 = 0
random.seed(4)

# 함수 정의 
def random_answer():
    return random.randint(0, 1)

# 30명의 응답 결과
for i in range(30):
    q1 = random_answer()
    q2 = random_answer()

    if q1 == 1 and q2 ==1:
     answer_Q1andQ2 +=1
    if q2 == 1 : answer_Q2 += 1
    if q1 == 1 or q2 == 1:
     answer_Q1orQ2 += 1

# 조건부 확률과 독립
print( "P(B|A):",answer_Q1andQ2/answer_Q2)
print( "P(B|O):",answer_Q2/ answer_Q1orQ2 )