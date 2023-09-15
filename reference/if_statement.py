#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# 파이썬에서 'if'문은 조건이 참(True)인지 거짓(False)인지를 검사하는데 사용됩니다.
# 조건이 참인 경우 'if' 블록 내의 코드가 실행되고, 그렇지 않으면 실행되지 않습니다.
# 또한, 'elif'와 'else'를 사용하여 더 많은 조건을 추가할 수 있습니다.

# 'and'와 'or'는 논리 연산자로, 여러 조건을 조합하는데 사용됩니다.
# 'and' 연산자: 모든 조건이 참이어야 전체가 참입니다 (&&와 동일).
# 'or' 연산자: 조건 중 하나 이상이 참이면 전체가 참입니다 (||와 동일).

# 예제 코드:
age = 18
has_license = True

# 'if-elif-else' 구조 사용 예
if age >= 18 and has_license:
    print("You are allowed to drive")
elif age >= 18 and not has_license:
    print("You are not allowed to drive without a license")
else:
    print("You are not allowed to drive")

# 'or' 연산자 사용 예
is_weekend = True
has_holiday = False

if is_weekend or has_holiday:
    print("You can relax today")
else:
    print("You have to work today")

# 이 코드는 'if' 문의 기본적인 사용법과 'and', 'or' 논리 연산자의 사용법을 보여줍니다.
# 여러 조건을 조합하여 복잡한 조건문을 만들 수 있습니다.
