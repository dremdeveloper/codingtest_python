#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
\
# "List comprehension"은 리스트를 생성하는 간결하고 효율적인 방법입니다.
# 기본 구조는 [expression for item in iterable if condition] 이며, 이 구조를 사용하여
# for 문과 if 문을 사용한 루프보다 더 간결하게 리스트를 생성할 수 있습니다.

# 예시 1: 0부터 9까지의 숫자로 리스트 생성
simple_list_comprehension = [x for x in range(10)]
print(simple_list_comprehension)  # 출력: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 예시 2: 0부터 9까지의 짝수로 리스트 생성
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # 출력: [0, 2, 4, 6, 8]

# 예시 3: 0부터 9까지의 숫자의 제곱으로 리스트 생성
squares = [x**2 for x in range(10)]
print(squares)  # 출력: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 예시 4: 두 리스트의 모든 가능한 쌍을 생성
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
pairs = [(x, y) for x in list1 for y in list2]
print(pairs)  # 출력: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

# List comprehension은 코드를 간결하게 만들고, 코드의 가독성을 향상시킵니다.
# 또한, 내부적으로 최적화되어 일반적인 for 루프보다 빠른 실행 시간을 제공합니다.
