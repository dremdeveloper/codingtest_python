#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 예제 리스트 생성
my_list = [10, 20, 30, 40, 50]

# 1. in 연산자
# `in` 연산자는 리스트에 특정 요소가 있는지 확인하는데 사용됩니다.

if 20 in my_list:
    print("20 is in the list!")  # 출력: 20 is in the list!

# 2. del 문
# `del`은 리스트의 특정 위치에 있는 요소를 삭제하는 데 사용됩니다.

del my_list[1]  # 인덱스 1의 요소 (20)를 삭제
print(my_list)  # 출력: [10, 30, 40, 50]

# 실수 예: 잘못된 인덱스로 접근
# del my_list[10]  # IndexError: list assignment index out of range

# 올바른 사용법: 삭제 전에 인덱스의 유효성 확인
index_to_delete = 10
if 0 <= index_to_delete < len(my_list):
    del my_list[index_to_delete]

# 실수 예: `in` 연산자의 효율성
# 큰 리스트에서 `in` 연산자를 사용하는 것은 비효율적일 수 있습니다. 
# 이는 `in` 연산자가 리스트 전체를 순회하면서 요소를 찾기 때문입니다.
large_list = list(range(1, 1000000))
# if 999999 in large_list:  # 이 연산은 리스트의 크기에 따라 시간이 오래 걸릴 수 있습니다.

# 올바른 사용법: 가능한 경우, 집합(set)과 같은 더 효율적인 자료구조를 사용
large_set = set(range(1, 1000000))
if 999999 in large_set:  # 집합에서의 멤버십 테스트는 평균적으로 더 빠릅니다.
    print("999999 is in the set!")  # 출력: 999999 is in the set!
