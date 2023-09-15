#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# 파이썬의 "zip" 함수는 여러 개의 이터러블(iterable) 객체 (예: 리스트, 튜플)의 요소들을 "포장"하여,
# 한 번에 하나씩 각 이터러블의 동일한 인덱스에 있는 요소들을 튜플로 그룹화하여 반환합니다.
# 이는 여러 이터러블의 데이터를 동시에 순회할 수 있게 해줍니다.
# zip 함수의 반환 값은 zip 객체이며, 이는 반복자이므로 리스트 또는 튜플로 변환하여 내용을 확인할 수 있습니다.

# 예시 1: 두 리스트를 zip 함수로 묶기
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
zipped = zip(list1, list2)
# zip 객체를 리스트로 변환하여 출력
print(list(zipped))  # 출력: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# 예시 2: 세 리스트를 zip 함수로 묶기
list3 = ['apple', 'banana', 'cherry', 'date']
zipped = zip(list1, list2, list3)
# zip 객체를 리스트로 변환하여 출력
print(list(zipped))  # 출력: [(1, 'a', 'apple'), (2, 'b', 'banana'), (3, 'c', 'cherry'), (4, 'd', 'date')]

# 예시 3: zip 함수와 for 루프 함께 사용
# 아래의 코드는 zip 함수를 이용하여 두 리스트의 요소를 동시에 순회하는 예입니다.
for num, letter in zip(list1, list2):
    print(f"{num} is paired with '{letter}'")  # 각 숫자와 문자가 페어로 출력됩니다.

# 참고: zip 함수는 가장 짧은 길이의 이터러블이 완료되면 중지됩니다.
# 따라서 이터러블의 길이가 다르면, zip 함수는 가장 짧은 이터러블의 길이에 맞춰서 그룹을 생성합니다.
