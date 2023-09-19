#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 에러 메시지: TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 의미: 두 개의 서로 다른 타입의 데이터를 연산하려고 할 때 발생하는 에러입니다.

# 에러 발생 코드
result = 5 + "10"

# 해결 방법:
# 연산 전에 데이터 타입을 일치시킵니다.
# 예:
# result = 5 + int("10")  # 또는 str(5) + "10"
