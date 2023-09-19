#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 소수 판별 알고리즘은 주어진 숫자가 소수인지 아닌지를 판별하는 알고리즘입니다.
# 소수는 1과 자기 자신 이외에 어떠한 수로도 나누어 떨어지지 않는 1보다 큰 양의 정수를 의미합니다.
# 이 알고리즘은 2부터 (입력받은 숫자의 제곱근 + 1)까지의 숫자로 나누어 볼 때,
# 한 번이라도 나누어 떨어지면 소수가 아니며, 모두 나누어 떨어지지 않으면 소수입니다.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 예시 사용법
print(is_prime(7))  # 출력: True
