#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 순열 생성 알고리즘은 주어진 리스트의 모든 가능한 순서의 조합을 생성하는 알고리즘입니다.
# itertools 모듈의 permutations 함수를 이용하여 리스트의 모든 순열을 생성할 수 있습니다.

from itertools import permutations

def generate_permutations(arr):
    return list(permutations(arr))

# 예시 사용법
arr = [1, 2, 3]
print(generate_permutations(arr))  # 출력: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
