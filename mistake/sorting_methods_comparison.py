#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# array.sort() vs sorted(array)

# 1. 문법과 개념 설명
# - array.sort()는 리스트 자체를 정렬하며 리턴값이 None입니다.
#   즉, 원본 리스트가 변경됩니다.
# - sorted(array)는 원본 리스트를 변경하지 않고, 새로운 정렬된 리스트를 반환합니다.

# 초기 리스트
numbers = [3, 1, 2, 4]

# 2. 어떻게 실수할 수 있는지

# 잘못된 사용법: array.sort()의 반환값을 다른 변수에 할당하려는 경우
sorted_nums = numbers.sort()  
print(sorted_nums)  # None이 출력됩니다. 이는 array.sort()가 반환하는 값이 None이기 때문입니다.

# 올바른 사용법
numbers.sort()  # 원본 리스트 자체를 정렬합니다.
print(numbers)  # [1, 2, 3, 4]가 출력됩니다.

# 3. 올바른 사용법

# sorted 함수를 사용하여 새로운 리스트에 정렬된 결과를 할당
correct_sorted_nums = sorted(numbers)
print(correct_sorted_nums)  # [1, 2, 3, 4]가 출력됩니다. 원본 리스트는 변경되지 않습니다.

# 추가 정보: sorted()는 리스트뿐만 아니라 어떤 iterable 객체도 받아 정렬된 리스트를 반환합니다.
string = "dcba"
sorted_string = sorted(string)
print(sorted_string)  # ['a', 'b', 'c', 'd']가 출력됩니다.
