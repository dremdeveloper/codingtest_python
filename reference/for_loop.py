#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# 파이썬에서 'for' 문은 시퀀스(리스트, 튜플, 문자열 등)의 항목들을 순차적으로 반복하여 처리하는 데 사용됩니다.
# 'for' 문은 'for 변수 in 시퀀스' 형식으로 작성되며, '변수'는 시퀀스의 각 항목을 참조하는 데 사용됩니다.

# 'and'와 'or'는 논리 연산자로, 여러 조건을 조합하는데 사용됩니다.
# 'and' 연산자: 모든 조건이 참이어야 전체가 참입니다 (&&와 동일).
# 'or' 연산자: 조건 중 하나 이상이 참이면 전체가 참입니다 (||와 동일).

# 'for' 문 예제:
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# 'and'와 'or' 연산자를 사용한 'for' 문 예제:
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number >= 2 and number <= 4:
        print(f"The number {number} is between 2 and 4")
    elif number < 2 or number > 4:
        print(f"The number {number} is outside the range of 2 and 4")

# 이 코드는 'for' 문의 기본 사용법과 'and', 'or' 논리 연산자의 사용법을 보여줍니다.
# 'and', 'or' 논리 연산자를 사용하여 'if' 문 내에서 여러 조건을 조합할 수 있습니다.
