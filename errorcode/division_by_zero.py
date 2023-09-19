#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
#에러 메시지: ZeroDivisionError: division by zero
# 의미: 숫자를 0으로 나눌 때 발생합니다. 수학적으로 0으로 나누는 것은 정의되지 않았으므로 프로그램이 이를 허용하지 않습니다.

# 에러 발생 코드
result = 10 / 0

# 해결 방법:
# 나누는 숫자(분모)가 0이 아닌지 확인하는 조건문을 사용하여 오류를 방지할 수 있습니다.
# 예:
# denominator = 0
# if denominator != 0:
#     result = 10 / denominator
# else:
#     print("Denominator cannot be zero.")
