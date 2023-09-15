#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# 파이썬에서 'while'문은 조건이 참(True)인 동안 반복적으로 코드 블록을 실행합니다.
# 'while'문의 구조는 'while 조건:'과 같으며, 조건이 참인 경우 'while' 블록 내의 코드가 계속 실행됩니다.

# 'and'와 'or'는 논리 연산자로, 여러 조건을 조합하는데 사용됩니다.
# 'and' 연산자: 모든 조건이 참이어야 전체가 참입니다 (&&와 동일).
# 'or' 연산자: 조건 중 하나 이상이 참이면 전체가 참입니다 (||와 동일).

# 'while'문 예제:
count = 0

while count < 5:
    print(f"Count is: {count}")
    count += 1  # count 변수를 1씩 증가시킵니다.

# 'and'와 'or' 연산자를 사용한 'while'문 예제:
value = 0

while value < 10:
    if value >= 3 and value <= 6:
        print(f"The value {value} is between 3 and 6")
    elif value < 3 or value > 6:
        print(f"The value {value} is outside the range of 3 and 6")
    value += 1  # value 변수를 1씩 증가시킵니다.

# 이 코드는 'while'문의 기본 사용법과 'and', 'or' 논리 연산자의 사용법을 보여줍니다.
# 'while'문을 사용하여 조건이 참인 동안 코드 블록을 반복적으로 실행할 수 있으며,
# 'and', 'or' 논리 연산자를 사용하여 여러 조건을 조합할 수 있습니다.
