#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# "map"과 "reduce" 함수는 iterable 객체를 효율적으로 처리할 수 있는 파이썬의 내장 함수입니다.

from functools import reduce

# 1. map 함수:
# map 함수는 각 요소에 함수를 적용한 결과를 반환하는 반복자를 생성합니다.
# 기본 구조는 "map(function, iterable)" 입니다.

# map 함수 사용 예:
numbers = [1, 2, 3, 4, 5]

# lambda 함수를 사용하여 각 요소를 제곱하고, map 객체를 반환합니다. 
# 이 때, lambda 함수가 리스트 numbers의 각 요소에 대해 한 번씩 호출됩니다.
squared_numbers = map(lambda x: x**2, numbers)

# map 객체를 리스트로 변환하여 결과를 확인합니다. 
# 여기에서 map 객체를 리스트로 변환하는 과정에서 실제로 lambda 함수가 호출되며, 각 요소를 제곱합니다.
print(list(squared_numbers)) # 출력: [1, 4, 9, 16, 25]


# 2. reduce 함수:
# reduce 함수는 iterable의 요소들을 차례대로 함수에 적용하면서 결과를 누적하여 최종 결과를 반환합니다.
# 기본 구조는 "reduce(function, iterable)" 입니다.

# reduce 함수 사용 예:
# reduce 함수를 사용하여 numbers 리스트의 모든 요소의 합계를 계산합니다. 
# 이 과정에서 lambda 함수가 첫 번째와 두 번째 요소를 더하고, 그 결과를 다음 요소와 더하는 과정을 반복하여 최종 결과를 반환합니다.
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# 최종 결과를 출력합니다.
print(sum_of_numbers) # 출력: 15

# 이렇게 map과 reduce 함수를 사용하면 복잡한 연산을 단순하고 효율적으로 수행할 수 있습니다.
