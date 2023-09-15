#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# 파이썬의 "range" 함수는 연속된 숫자의 시퀀스를 생성하는 데 사용됩니다. 
# 이 함수는 주로 for 루프와 함께 사용되며, 세 가지 다른 형태의 인자를 가질 수 있습니다: 
# 1. range(stop): 0부터 'stop - 1'까지의 숫자 시퀀스를 생성합니다.
# 2. range(start, stop): 'start'부터 'stop - 1'까지의 숫자 시퀀스를 생성합니다.
# 3. range(start, stop, step): 'start'부터 'stop - 1'까지의 숫자 시퀀스를 생성하되, 'step' 간격으로 숫자를 생성합니다.

# 1. range(stop) 형태의 사용 예:
# 아래 코드는 0부터 4까지의 숫자를 출력합니다.
for i in range(5):
    print(i) # 출력: 0, 1, 2, 3, 4

print("---------")

# 2. range(start, stop) 형태의 사용 예:
# 아래 코드는 5부터 9까지의 숫자를 출력합니다.
for i in range(5, 10):
    print(i) # 출력: 5, 6, 7, 8, 9

print("---------")

# 3. range(start, stop, step) 형태의 사용 예:
# 아래 코드는 0부터 9까지의 숫자 중, 2 간격으로 숫자를 출력합니다.
for i in range(0, 10, 2):
    print(i) # 출력: 0, 2, 4, 6, 8
