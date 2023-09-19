#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 이진 탐색 알고리즘은 정렬된 리스트에서 특정 원소를 빠르게 찾기 위한 알고리즘입니다.
# 이 알고리즘은 리스트의 중간값을 기준으로 찾고자 하는 값이 중간값보다 큰지 작은지를 판단하며,
# 이를 반복하여 원하는 값을 찾습니다.
# 이진 탐색은 O(log n)의 시간 복잡도를 가지며, 리스트가 정렬된 상태에서만 사용할 수 있습니다.

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 예시 사용법
arr = [1, 2, 3, 4, 5]
print(binary_search(arr, 3))  # 출력: 2
