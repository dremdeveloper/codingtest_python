#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 조합 생성 알고리즘은 주어진 리스트에서 n개의 원소를 선택하는 모든 가능한 조합을 생성하는 알고리즘입니다.
# itertools 모듈의 combinations 함수를 이용하여 리스트에서 n개의 원소를 선택하는 모든 조합을 생성할 수 있습니다.

from itertools import combinations

def generate_combinations(arr, n):
    return list(combinations(arr, n))

# 예시 사용법
arr = [1, 2, 3]
print(generate_combinations(arr, 2))  # 출력: [(1, 2), (1, 3), (2, 3)]
