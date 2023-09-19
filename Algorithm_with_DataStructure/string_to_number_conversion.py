#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 문자열을 숫자로 변환하는 알고리즘은 문자열 형태의 숫자를 실제 정수 또는 실수 형태로 변환하는 알고리즘입니다.
# Python에서는 int() 함수를 사용하여 문자열을 정수로, float() 함수를 사용하여 문자열을 실수로 변환할 수 있습니다.

def string_to_number(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return "변환 불가"

# 예시 사용법
print(string_to_number("123"))  # 출력: 123
