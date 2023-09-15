#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# 파이썬에서 try-except 블록은 프로그램 실행 중 발생할 수 있는 에러를 처리하기 위해 사용됩니다.
# 'try' 블록 내에서 코드를 실행하다가 에러가 발생하면, 'except' 블록이 실행되며 프로그램이 중단되지 않습니다.
# 이러한 방식으로, 프로그래머는 에러를 예측하고 적절히 대응할 수 있습니다.

# 기본 사용 방법은 다음과 같습니다:
# try:
#     # 에러가 발생할 가능성이 있는 코드
# except <에러 종류>:
#     # 에러 발생 시 실행될 코드

# 아래 예제에서, 우리는 0으로 나누는 에러(ZeroDivisionError)와 
# 존재하지 않는 리스트의 인덱스를 참조하는 에러(IndexError)를 처리합니다.

try:
    # 0으로 나누기 시도 (ZeroDivisionError 발생)
    result = 10 / 0
except ZeroDivisionError:
    # ZeroDivisionError 발생 시 이 블록이 실행됩니다.
    result = None
    print("Error: Cannot divide by zero")

# result 변수가 None이므로, 에러가 발생했음을 알 수 있습니다.
print(f"Result of division: {result}")

# 리스트 인덱스 에러 처리 예제
try:
    # 리스트 선언
    my_list = [1, 2, 3]
    # 존재하지 않는 인덱스 참조 시도 (IndexError 발생)
    value = my_list[10]
except IndexError:
    # IndexError 발생 시 이 블록이 실행됩니다.
    value = None
    print("Error: Index out of range")

# value 변수가 None이므로, 에러가 발생했음을 알 수 있습니다.
print(f"Value from list: {value}")
