# 컴프리헨션과 이터레이터 개념을 이해하고
# 파이썬의 반복 처리 구조를 효율적으로 사용
# 컴프리헨션(Comprechension)
# List, set, dict
# 파이썬 자료를 효울적으로 간결하게
# 반복문과 조건문을 사용
# 리스트 컨프리헨션(리스트를 짧고 간결하게)
# nums = [1,2,3,4]
# print("nums :", nums)
# squares = [n ** 2 for n in nums]
# print("squares : ", squares)
# **은 제곱을 구한다.
# 짝수만 출력하기
# nums = [1,2,3,4,5]
# print("nums : ", nums)
# evens = [n for n in nums if n%2 ==0]
# print("evens: ", evens)
# nums = [1,2,3,4,5]
# for i in nums:
#     if i % 2 == 0:
#      print(i)
# nums = [1,2,3,4,5]
# a =[]
# for xx in nums:
#     if xx % 2 == 0:
#      a.append(xx)
# print(a)
# nums = [1,2,3,4,5]
# print("nums:", nums)
# a = [b for b in nums if b % 2 == 0]
# print("a:",a)
#리스트 컴프레헨션을 사용해서 문자열의 길이 구하기
# names = ["kim", "lee", "park"]
# # 결과를 담을 빈 리스트 생성
# lengths =[]
# for n in names:
#     m =len(n)
#     lengths.append(m)
# print(lengths)    
# 컨프리헨션 사용해서 한줄로 만들기
# names = ["kim", "lee", "park"]
# lengrhs = [len(name) for name in names]
# print(lengrhs)
# 제곱을 하는 코드
# 값을 추가할 때 append()를 사용하지 않아도 자동으로 추가한다.
# 딕셔너리 컴프리헨션
# nums = [1,2,3,4,5]
# print("nums:", nums)
# square_dict = {n : n**2 for n in nums}
# print("square_dict : ", square_dict)
# 짝수만 출력
nums = [1,2,3,4,5]
print("nums:", nums)
even_dict = {n : "even" for n in nums if n % 2 ==0}
print(even_dict)
# even은 다른걸로 수정 가능
# 이터레이터(하나씩 값을 꺼냄)
# Iterator: next함수 사용
# 이터레이터는 하나의 '다음' 값을 꺼내올 수 있는 객체
nums = [1,2,3,4,5]
# iter()함수사용
# it : 이터레이터의 약자
it = iter(nums)
#리스트는 반복 가능한 객체이므로 이터러블
# print(next(it)) -> 다음값꺼내기
# print(next(it))
# print(next(it))
# print(next(it))
# 반복만 할수 있으면 이터러블
# 리스트나 딕셔너리도 꺼낼수 있지만
# 리스트나 딕셔너리는 생성되는 순간
# 내부의 모든 데이터를 메모리에 저장한다.
# 그러나 데이터의 양이 많아질수록 사용량이 증가한다는 단점이 있다.
# 이터레이터의 사용 이유
# 메모리를 한번에 올리지 않고 필요할 때마다 하나씩 생성하여 반환 해준다.
# 특징:next()로 하나씩 꺼낸다.
# 어디까지 꺼냈는지 기억한다.(상태유지)
# 다 꺼내면 Stoplteration 발생
# 한 번 쓰면 끝 (소모성)
# 로그 데이터
# DB결과/ 크롤링 데이터
# API응답 스트리밍
# 대용량 데이터를 한번에 메모리에 올리지 않고 순차적으로 처리해야 하는 분야에서 자주 사용한다.
# "순차 접근만 가능" 따라서 인덱스로 바로 점프 기본적으로 불가능
# 리스트는 num[5]처럼 특정 위치에 바로 접근할 수 있지만,
# 이터레이터는 next()를 통해 앞에서부터 하나씩 이동해야 한다.
# range()함수나 itertools.islice()같은 도구를 사용하면 원하는 구간을 건너뛸 수는 있다.
# 하지만 내부적으로는 결국 앞에서부터 순차적으로 이동한다.
# 이터레이터는 메모리를 적게 사용하여 데이터를 순차적으로 처리하기 위해 만들어진 구조이다.
# 이터레이터는 "흐름"을 다루는 구조이지, "위치"를 다루는 구조가 아니다.