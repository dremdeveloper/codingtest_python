#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# 파이썬에서 'lambda'는 익명 함수를 생성하는 데 사용되는 키워드입니다. 
# 'lambda' 함수는 일반 함수(def)와 같지만, 이름 없이 정의되며, 한 줄로 표현됩니다.
# 기본 구조는 다음과 같습니다: lambda arguments: expression
# 'lambda' 함수는 다양한 케이스에서 사용될 수 있으며, 일회성의 간단한 함수나 다른 함수의 인자로 전달될 수 있습니다.

# 1. 기본적인 lambda 함수:
add = lambda x, y: x + y
# 사용 예:
print(add(1, 2))  # 출력: 3

# 2. 리스트의 sort 메서드에서 key 인자로 사용:
# lambda 함수를 사용하여 리스트의 각 요소에 대한 정렬 키를 지정할 수 있습니다.
my_list = [(1, 2), (3, 1), (5, 0), (4, 5)]
my_list.sort(key=lambda x: x[1])
# 사용 예:
print(my_list)  # 출력: [(5, 0), (3, 1), (1, 2), (4, 5)]

# 3. filter 함수에서 사용:
# lambda 함수를 사용하여 iterable에서 특정 조건을 만족하는 요소만 필터링할 수 있습니다.
nums = [0, 1, 2, 3, 4, 5]
even_nums = filter(lambda x: x % 2 == 0, nums)
# 사용 예:
print(list(even_nums))  # 출력: [0, 2, 4]

# 4. map 함수에서 사용:
# lambda 함수를 사용하여 iterable의 모든 요소에 함수를 적용할 수 있습니다.
nums = [0, 1, 2, 3, 4, 5]
squares = map(lambda x: x ** 2, nums)
# 사용 예:
print(list(squares))  # 출력: [0, 1, 4, 9, 16, 25]

# 5. reduce 함수에서 사용:
# lambda 함수를 사용하여 iterable의 모든 요소를 단일 값으로 줄일 수 있습니다.
from functools import reduce
nums = [1, 2, 3, 4, 5]
sum_of_nums = reduce(lambda x, y: x + y, nums)
# 사용 예:
print(sum_of_nums)  # 출력: 15
