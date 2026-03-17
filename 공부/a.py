#조건문:싱황에따라 다르게 실행
#num =int(input("첫번째 숫자: "))
#operator = input("연산자 입력(+, -, -, *, /) ")
#num2 = int(input("두번째 숫자: "))
#if operator == "+":
#    print("결과 :", num + num2)
#elif operator == "-":
#   print("결과 :", num - num2)
#elif operator == "*":
#   print("결과 :", num * num2)
#elif operator == "/":
#    if num2 == 0:
#       print("0으로 나눌 수 없습니다.")
#   else:
#       print("결과 :", num / num2)
#else:    print("잘못된 연산자입니다.")
#숫자0으로 나눗셈을 할때 오류

#반복문
# count = 10
# while count > 7:
#     print(count)
#     count -= 1
# money = 5000 #내가 가지고 있는 돈
# count = 1     #반복하는 횟수
# while money >= 3000:
#     print(f"아이스크림을 {count}번 사먹었습니다.")
#     print(f"남은 금액은 {money}원 입니다.")
#     print("----")
#     money -= 1000
#     count += 1
# while문 사용하기: 계속 반복되는 부문 시스템(메뉴판)
# 메뉴판을 먼저 보여주는 print문을 사용할 것이다.
# while문의 조건을 blooean이라는 내용으로 사용하겠다.
#반복문으로 계속 메뉴를 시켜주세요. 종료라는 메뉴를 선택하면 종료
#변수 하나 만들어 줄것(조건식)
# blooean = True
# print("무인매장입니다. 방문해주셔서 감사합니다.")
# print("메뉴판입니다.")
# print("1. 아이스크림")
# print("2. 음료수")
# print("3. 햄버거")
# print("4. 종료")
# while blooean:
#     choice =input("\n메뉴를 선택해주세요: ")
#     if choice == "1":
#         print("아이스크림을 선택하셨습니다.")
#     elif choice == "2":
#         print("음료수를 선택하셨습니다.")
#     elif choice == "3":
#         print("햄버거를 선택하셨습니다.")
#     elif choice == "4":
#         print("종료를 선택하셨습니다. 이용해주셔서 감사합니다.")
#         blooean = False
# 반복문:for문 반복의 횟수를 알고 있을 때 사용한다. for문은 리스트, 튜플, 딕셔너리, 문자열 등과 같은 시퀀스 자료형에서 사용할 수 있다.   
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     print(num)
# str = "Hello"
# for char in str:
#     print(char)  
# name =["Tom", "Jane", "Bob"]
# for ch in name:
#     print(ch)    
#문자열은 하나의 데이터
# 리스트는 안에 어떤 값이 있든 데이터 타입이 리스트이기 때문에
# for문 같은 경우 참조형 데이터 타입을 많이 사용한다.
#for문을 사용한 합계산
# nums = [1, 2, 3, 4, 5]
# sum = 0
# for i in nums:
#     sum = sum + i
# print(sum)
sum = 0
for i in range(1, 16):
    sum += i
print(sum)
# 반목문을 사용하는 이유
# 직접 코드를 입력시 시간이 오래 걸림
# for문 변수 in 리스트:
#     실행할 코드
# range(시작값, 끝값, 간격) : 시작값부터 끝값까지 간격만큼 증가하는 숫자 시퀀스를 생성하는 함수
# range(1, 16) : 1부터 15까지의 숫자 시퀀스를 생성한다. 끝값은 포함되지 않음
# 리스트: 여러 개의 값을 하나의 변수에 저장할 수 있는 데이터 타입
# nums: [] 대괄호 사용, 중복허용, 순서 있음, 수정 가능  
# 자료형(요소와 인덱스)
# animals = ["cat", "dog", "rabbit"]
# print(animals)
# 리스트:요소(Element)와 인덱스(Index)
# 요소: 리스트 안에 있는 각각의 값
# 인덱스: 리스트 안에 있는 요소의 위치를 나타내는 숫자
example = [1,2.2,True,"Y"]
# print(example)
# 특정값만 가져올수 있고 파이썬에서만 사용가능
# print(example[0])
# print(example[1])
# print(example[2])
# print(example[3])
example[1]=3.4
print(example[1])
print(example)
# 음수의 인덱스로 출력해보기
print(example[-3])
print(example[-1])
# 양수, 음수, 인덱스를 활용해서 값을 꺼내기
names =["kim", "lee", "park","choi","min", "jung","jeon"]
print(names[2])
print(names[4])
print(names[-4])
print(names[-6])