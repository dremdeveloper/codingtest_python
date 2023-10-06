#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
import math  # math 모듈 사용

# 1. ** 연산자
# **는 파이썬의 거듭제곱 연산자입니다. 가장 직관적이며 일반적으로 사용됩니다.
result1 = 2 ** 3
print(result1)  # 8

# 2. pow 함수
# pow는 내장 함수로써 2개 혹은 3개의 인자를 받습니다.
result2 = pow(2, 3)  # 2의 3승
print(result2)  # 8

# pow 함수의 세 번째 인자는 모듈로 연산에 사용됩니다.
result3 = pow(2, 3, 3)  # (2의 3승) % 3
print(result3)  # 2

# 3. math.pow 함수
# math.pow는 math 모듈에 있는 함수로, 항상 float 값을 반환합니다.
result4 = math.pow(2, 3)
print(result4)  # 8.0

# 실수 예: 반환 값의 타입을 고려하지 않고 정수 연산을 수행하려고 할 때
# int_result = math.pow(2, 3) + 1  # 결과는 float 값이 됩니다.
# 올바른 방법: float 값을 int로 변환하여 사용
int_result = int(math.pow(2, 3)) + 1
print(int_result)  # 9

# **와 pow는 거의 동일한 연산을 수행하지만, 모듈로 연산이 필요한 경우나 float 반환 값이 필요한 경우에 따라 적절한 함수나 연산자를 선택해야 합니다.
