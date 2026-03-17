# 세트
# set_str ={"ABC"}
# print(set_str)
# # 타입을 확인해보기 :type()
# print(type(set_str))
# # 순서없고 중복허용 x
# set_str ={"ABC","DEF","ABC"}
# print(set_str)
# 리스트면 다 나오는데 세트는 중복빼고 출력
# 리스트를 세트로 변환하기: set()
# num_list = [1,2,3]
# print(num_list)
# set_list =set(num_list)
# print(type(set_list))
# print(set_list)
# # 세트는 중복 허용 하지 않음
# 인덱스 없음(순서없음)
# 여러개의 값을 하나로 묶어서 저장
# 세트의 핵심 특징은 중복제거이다
# set의특징 확인하기
# str_banana = "banana"
# set_banana = set(str_banana)
# print(set_banana)
# # 중복허용하지 않기 때문에
# print(set_banana)
# print(set_banana[0])
# 위에 처럼 하면 오류발생
# 세트의 요소
# 만약 요소에 접근하고 싶다면 set를 리스트 또는 튜플로 변환하여 접근
# 값이 달라진다 :순서가 없다
# str_banana = "banana"
# set_banana = set(str_banana)
# print(set_banana)
# # 세트를 리스트나 튜플로 바꾸겠다.
# list_banana =list(set_banana)
# tuple_banana = tuple(set_banana)
# print(list_banana[0])
# print(tuple_banana[0])
# # 인덱스로 가져올 수는 있지만 원하는 값이 안나올 수 있다.
# # 딕셔너리
# # 딕셔너리는 키와 값 쌍으로 이뤄진 자료형이다.
# # 가장 많이 사용되는 컬렉션 중 하나이다.
# # Dictionary:키(key)와 값(value) 쌍으로 이루어진 자료형
# # 특징: 중괄호 사용{}, 값 변경 (수정, 삭제, 추가) 가능
# # key는 중복불가, 값은 중복허용
# person = {
#     "name":"tom",
#     "age" :20,
#     "phone" : "010-1234-5678",
#     "subject" :["python","java"]
# }
# print(person)
# print(person["name"])
# print(person["age"])
# print(person["subject"])
# # 딕셔너리 값 추가하기
# dic_color = {
#     "Red" : "apple",
#     "Yellow" : "banana",
#     "Puple" : "grape"
# }   
# print(dic_color)
# # 값을 추가 할 것이다.
# dic_color["Orange"] = "orange"
# print(dic_color)
# # 딕셔너리 값 삭제하기
# 모든 키값을 추출해주는 함수 :keys()
# sports_star = {
#     "축구" : "손흥민",
#     "피겨" : "김연아",
#     "수영" : "박태환"}
# print(sports_star.keys())
# # 반복문을 사용해 하나씩 꺼낼 수 있다.
# for key in sports_star.keys():
# # sports_star라는 딕셔너리에 모든 키값을 추출하겠다.
# # 반복문을 사용하고 가져온 하나의 키값들을 key라는 변수에 넣겠다.
#     print(f"꺼낸 키:{key}")
#     print(f"값 꺼내기 : {sports_star[key]}")
# 딕셔너리에 모든값 Value을 추출하는 함수 :Values()
abc_dic ={
    "a":"zaa",
    "b":"caa",
    "d":"vaa",
}
# print(abc_dic.values())
# 반목문을 사용해서 하나씩 가져올 수 있다.
# for a in abc_dic.values():
#     print(a)
# 모든 key-value를 추출하는 함수 : items()
print(abc_dic.items())
# 키와 값을 구분하기 쉽게 추출해준다.
for a in abc_dic.items():
    print(a)
# 정렬을 해주는 함수: sorted()
python_grade = {
    "kelly" : "B",
    "json" : "A",
    "ian" : "C",
    "elly" : "D"
    }
print(f"기존 순서 : {python_grade}")
print(f"오름차순 정렬 : {sorted(python_grade.items())}")
# 키값을 기준으로 정렬을 하는 함수 sorted()를 사용
# 기본적으로 오름차순으로 정렬을 한다.
print(f"내림차순 정렬 : {sorted(python_grade.items(),reverse=True)}")
# 알파벳 기준으로 오름차순 내림차순 결정
# 내림차순 사용 방법 : sorted(정렬을 해야하는 데이터, 정렬방법)
# reverse = True