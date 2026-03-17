# 리스트를 활용하는 확장된 기능을 사용할 것이다.
# 1. 리스트를 잘라내는 기능 (슬라이싱)
# [start:stop]
# example = [1,2.2,True,"Y"]
# print(example[0:2])
# # 0:2는 시작은 0부터 시작해라
# # 끝나는 지점은 2인데 실제 실행은 -1요소까지 실행
# # [start:stop:step]
# print(example[0:4:2])
# # 2칸씩 건너 뛰어라
# # 리스트,튜플,세트,딕셔너리
# # 리스트 요소 추가하기
# # append() : 리스트의 끝에 요소를 추가하는 메서드
# # extend() : 리스트에 다른 리스트의 요소를 추가하는 메서드
# # insert() : 리스트의 특정 위치에 요소를 추가하는 메서드
# a = [1, 2, 3]
# print(a)
# a.append(4)
# print(a)
# # 어떤 변수에다가 함수를 사용하겠다.:"."
# a = [1, 2, 3]
# print(a)
# b = [4, 5, 6]
# a.extend(b)
# print(a)
# a =[1,2,3]
# print(a)
# a.insert(1,10)
# print(a)
# 리스틀르 삭제하는 기능(pop,remove)
# colors = ["black", "yellow","red","black"]
# print(f"삭제 전 : {colors}")
# # colors.pop(3)
# colors.pop()
# print(f"3번 인덱스 삭제 후: {colors}")
# #pop에 아무것도 입력하지 않으면 끝에 데이터 요소가 사라짐
# remove() :특정 값을 가진 요소를 삭제하는 기능
# nums = [1,2,3,4,5]
# print(nums)
# nums.remove(3)
# print(nums)
# #원래는 pop을 쓰면 0부터 계산하면 4가 없어져야 하는데
# #remove는 특정값을 지워줌
# # clear():리스트를 전체 삭제하는 기능
# nums.clear()
# print(nums)
# 리스트의 유용한 메서드(함수)
# 메서드:만들어져 있는 기능
# 관리를 편하게 하기 위한 기능
# 파이썬에서 제공해주는 기능
# len():리스트의 길이 반환
# cs = ["데이터","알고리즘","파이썬"]
# cs_length = len(cs)
# print(cs_length)
# sort(),sort(revers=True)
# sort():리스트를 정렬해주는 기능
# list_num = [2,7,3,5]
# list_num.sort()
# print(f"올림차순 정렬: {list_num}")
# list_num.sort(reverse=True)
# print(f"내림차순 정렬 : {list_num}")
# # sorted():새로운 리스트
# numbers = [5,2,4,1,3]
# print(f"원본: {numbers}")
# sorted_numbers = sorted(numbers)
# print(f"sorted: {sorted_numbers}")
# 새로운 리스트에다가 정렬을 하고, 원본 데이터는 보존
# reverse():리스트의 요소의 순서를 반전
# numbers.reverse()
# print(f"순서 반전 : {numbers}")
# # 정렬이 아닌 그 순서를 반전 시켜준다.
# numbers = [5,4,1,6,9]
# print(f"{4 not in numbers}")
# print(f"{4 in numbers}")
# # 4있다면 true 없다면 false
# # join():리스트의 요소들을 문자열로 반환
# list_abc = ["a", "b","c"]
# result = "-".join(list_abc)
# print(result)
# # "*"이라는 기호를 넣어서 출력
# result2 = "*".join(list_abc)
# print(result2)
# result3 = "".join(list_abc)
# print(result3)
# #리스트의 기능은 많다 대표적인 것만 사용해봄
# # 순서있다/중복가능/대괄호
# # 튜플(tuple)리스트와 거의동일하지만
# # 불변이라는 특성을 가진다.
# # 소괄호()사용/값변경,추가,삭제 불가/중복허용
# names = ("kim","lee","park")
# first_name = names[0]
# second_name = names[1]
# last_name = names [2]
# print(first_name)
# print(second_name)
# print(last_name)
# #튜플 값을 변경하면?
# names[0] ="jeon"
# 튜플의 유용한 메서드(함수)
# count():특정값을 가진 요소의 개수
# ex) a라는 값이 몇개인지
alp = ("a","a","b","b","b","c")
print(alp.count("a"))
print(alp.count("b"))
print(alp.count("c"))
# index( ): 특정값을 가진 요소의 인덱스를 반환
print(alp.index("a"))
# 여러개의 인덱스가 존재하더라도
# 찾는 것의 가장 첫번째 요소(위치)를 가져온다.