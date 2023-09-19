#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 에러 메시지: ValueError: invalid literal for int() with base 10: 'ten'
# 의미: 올바르지 않은 값이 주어졌을 때 발생하는 에러입니다.

# 에러 발생 코드
result = int('ten')

# 해결 방법:
# 올바른 값을 제공하거나, try-except 블록을 사용하여 오류를 처리합니다.
# 예:
# try:
#     result = int('ten')
# except ValueError:
#     print("Invalid input")
