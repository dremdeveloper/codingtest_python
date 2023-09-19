#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 에러 메시지: TypeError: function_name() missing 1 required positional argument: 'arg'
# 의미: 함수 호출 시 필요한 인자가 누락되었을 때 발생합니다.

def function_name(arg):
    print(arg)

# 에러 발생 코드
function_name()

# 해결 방법:
# 함수 호출 시 필요한 모든 인자를 제공하여 오류를 방지할 수 있습니다.
# 예:
# function_name(arg="Hello")
