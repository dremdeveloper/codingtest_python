#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# range 함수의 기본적인 문법:
# range([start], stop, [step])
# start: 시작 값 (생략 가능, 기본값은 0)
# stop: 종료 값 (필수, 생성되는 숫자는 이 값 바로 전까지)
# step: 간격 (생략 가능, 기본값은 1)

# 0부터 4까지의 숫자를 생성합니다.
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4를 순서대로 출력합니다.

# 2부터 8까지 2 간격으로 숫자를 생성합니다.
for i in range(2, 9, 2):
    print(i)  # 2, 4, 6, 8을 순서대로 출력합니다.

# 실수 예: stop 값을 포함하여 숫자를 생성하려고 할 때
# 아래의 코드는 5를 출력하지 않습니다.
# for i in range(1, 5):
#     print(i)

# 올바른 방법: stop 값을 포함하여 숫자를 생성하려면
# stop 값에 1을 더합니다.
for i in range(1, 6):  # 1부터 5까지 출력합니다.
    print(i)

# 실수 예: step 값이 0인 경우
# 아래의 코드는 무한 루프에 빠질 위험이 있습니다.
# for i in range(1, 5, 0):
#     print(i)

# 올바른 방법: step 값은 0이 아닌 다른 값을 사용합니다.
for i in range(1, 5, 1):
    print(i)  # 1, 2, 3, 4를 순서대로 출력합니다.

# 실수 예: start 값이 stop 값보다 크고, step이 양수인 경우
# 아래의 코드는 아무 것도 출력하지 않습니다.
# for i in range(5, 1):
#     print(i)

# 올바른 방법: start 값이 stop 값보다 클 경우, step을 음수로 설정하여 역순으로 숫자를 생성합니다.
for i in range(5, 1, -1):
    print(i)  # 5, 4, 3, 2를 순서대로 출력합니다.
