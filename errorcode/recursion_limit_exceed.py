#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 에러 메시지: RecursionError: maximum recursion depth exceeded
# 의미: 재귀 함수 호출이 너무 깊어져 Python의 최대 재귀 깊이 제한을 초과할 때 발생합니다.

# 에러 발생 코드
def recursive_function(n):
    return recursive_function(n+1)

recursive_function(0)

# 해결 방법:
# 재귀 함수에 종료 조건을 추가하여 오류를 방지할 수 있습니다.
# 예:
# def recursive_function(n):
#     if n == 100:  # 종료 조건
#         return n
#     return recursive_function(n+1)
