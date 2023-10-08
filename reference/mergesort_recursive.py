#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 머지 정렬(Merge Sort)의 개념:
# - 머지 정렬은 분할 정복(divide and conquer) 전략을 사용하는 정렬 알고리즘입니다.
# - 배열을 절반으로 계속해서 분할하다가 길이가 1이 되면, 이를 기준으로 다시 합치면서 정렬합니다.
# - 두 부분 배열을 합치는 과정(merge)에서 정렬이 이루어집니다.
# - 머지 정렬은 안정적인 정렬로, 순서가 같은 원소들의 상대적 순서가 정렬 후에도 유지됩니다.

# 시간 복잡도:
# - 머지 정렬의 시간 복잡도는 O(n log n)입니다.
# - 배열을 절반씩 분할하는 데 log n의 시간이 걸리고, 각 분할마다 n의 연산이 필요하므로 n log n이 됩니다.

# 예시: arr = [38, 27, 43, 3, 9, 82, 10]
# 머지 정렬 과정 도식화:
# 1. 원래 배열을 절반씩 분할
# arr -> [38, 27, 43, 3] and [9, 82, 10]
# 
# 2. 각각의 배열을 다시 절반씩 분할 (재귀적으로 반복)
# [38, 27, 43, 3] -> [38, 27] and [43, 3]
# [9, 82, 10] -> [9] and [82, 10]
# 
# 3. 분할된 배열들을 정렬하면서 병합
# [38, 27] -> 27, 38
# [43, 3] -> 3, 43
# [82, 10] -> 10, 82
# 
# 4. 다시 이전 단계의 정렬된 배열들을 병합
# [27, 38] and [3, 43] -> 3, 27, 38, 43
# [9] and [10, 82] -> 9, 10, 82
# 
# 5. 최종적으로 병합하여 완전히 정렬된 배열을 얻음
# [3, 27, 38, 43] and [9, 10, 82] -> 3, 9, 10, 27, 38, 43, 82

# 병합 정렬 함수
def merge_sort(arr):
    # 재귀 종료 조건: 리스트의 길이가 1 이하면 이미 정렬된 것으로 간주하고 반환합니다.
    if len(arr) <= 1:
        return arr

    # 리스트를 중간 지점에서 분할합니다.
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # 왼쪽 부분 리스트를 재귀적으로 정렬합니다.
    right = merge_sort(arr[mid:])  # 오른쪽 부분 리스트를 재귀적으로 정렬합니다.

    # 두 부분 리스트를 병합합니다.
    return merge(left, right)

# 병합 함수
def merge(left, right):
    result = []  # 병합된 결과를 저장할 리스트를 초기화합니다.
    i = j = 0  # 왼쪽과 오른쪽 부분 리스트를 가리키는 인덱스를 초기화합니다.

    # 두 부분 리스트를 비교하면서 작은 값을 결과 리스트에 추가합니다.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 원소들을 결과 리스트에 추가합니다.
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# 주어진 리스트를 정렬합니다.
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)

# 정렬된 결과를 출력합니다.
print(sorted_arr)
