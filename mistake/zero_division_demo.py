#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 실수 예: 0으로 나누기
# result = 10 / 0  # ZeroDivisionError: division by zero

# 파이썬에서 숫자를 0으로 나누려고 하면 ZeroDivisionError가 발생합니다.

# 실수 예: 변수를 사용하여 나누기를 수행하되, 변수 값이 0인 경우
denominator = 0
# if denominator is not 0:
#     result = 10 / denominator  # 이 줄도 ZeroDivisionError를 발생시킵니다.

# 올바른 사용법: 나눗셈을 수행하기 전에 분모가 0인지 확인
if denominator != 0:
    result = 10 / denominator
    print(result)
else:
    print("Cannot divide by zero!")

# 특히 복잡한 계산이나 사용자 입력을 처리할 때는 이러한 오류가 발생할 수 있으므로 주의가 필요합니다.
# 사용자 입력을 받아서 나눗셈을 수행하는 경우:

# user_input = float(input("Enter a number to divide 10 by: "))
# if user_input != 0:
#     print(10 / user_input)
# else:
#     print("Cannot divide by zero!")
