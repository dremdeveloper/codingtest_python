#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 구간 합 알고리즘은 배열이 주어졌을 때 특정 구간의 원소들의 합을 구하는 알고리즘입니다.
# 구간은 시작 인덱스와 종료 인덱스로 정의되며, sum 함수를 이용하여 해당 구간의 합을 계산할 수 있습니다.

def interval_sum(arr, start, end):
    return sum(arr[start:end+1])

# 예시 사용법
arr = [1, 2, 3, 4, 5]
print(interval_sum(arr, 1, 3))  # 출력: 9
