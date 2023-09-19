#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 시간 측정 알고리즘은 코드의 실행 시간을 측정하는 알고리즘입니다.
# Python의 time 모듈을 사용하여 특정 코드 블록 또는 함수의 실행 시간을 측정할 수 있습니다.

import time

def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

# 예시 사용법
def sample_function():
    for _ in range(1000000):
        pass

print(measure_time(sample_function))  # 출력: 실행 시간(초)
