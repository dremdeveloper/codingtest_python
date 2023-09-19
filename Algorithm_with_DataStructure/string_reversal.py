#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 문자열 뒤집기는 주어진 문자열의 문자들의 순서를 반대로 만드는 알고리즘입니다.
# Python에서는 문자열 슬라이싱을 이용해 이를 간단히 구현할 수 있으며,
# s[::-1] 형태로 사용하면 문자열 s를 뒤집어 줍니다.

def reverse_string(s):
    return s[::-1]

# 예시 사용법
print(reverse_string("Hello"))  # 출력: "olleH"
