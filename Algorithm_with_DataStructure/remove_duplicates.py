#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 중복 원소 제거 알고리즘은 리스트에서 중복되는 원소를 제거하는 알고리즘입니다.
# Python에서는 set 자료형을 이용하여 쉽게 중복을 제거할 수 있으며,
# 이를 다시 list로 변환하여 중복이 제거된 리스트를 얻을 수 있습니다.

def remove_duplicates(arr):
    return list(set(arr))

# 예시 사용법
arr = [1, 2, 2, 3, 3, 4]
print(remove_duplicates(arr))  # 출력: [1, 2, 3, 4] (순서는 변할 수 있음)
