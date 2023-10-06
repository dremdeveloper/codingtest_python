#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 정렬된 리스트 생성
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 실수 예: 잘못 짠 이분 탐색
def incorrect_binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid  # 여기서 mid + 1이 되어야 합니다.
        else:
            high = mid  # 여기서 mid - 1이 되어야 합니다.

    return -1

# 위의 코드는 잘못된 업데이트 방식 때문에 무한 루프에 빠질 수 있습니다.

# 올바른 사용법: 이분 탐색
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1  # 올바르게 범위를 조정
        else:
            high = mid - 1  # 올바르게 범위를 조정

    return -1

print(binary_search(sorted_list, 5))  # 올바르게 4를 출력
