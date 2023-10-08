#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 에라토스테네스의 체 개념:
# 주어진 범위 내에서 연속적인 숫자를 나열하고, 
# 가장 작은 수부터 그 수의 배수를 제거해 나가면서 소수만을 남기는 방법.
# 예: 2부터 시작하여 2의 배수를 제거, 다음 최소값인 3의 배수를 제거, 
# 이후 5의 배수, 7의 배수를 차례대로 제거... (n의 제곱근까지)

# 시간 복잡도:
# 에라토스테네스의 체의 시간 복잡도는 O(n log log n)으로, 
# n 이하의 모든 소수를 효율적으로 찾을 수 있습니다.

# 도식화:
# e.g., n = 30, current = 2:
# 시작: [F, F, T, T, T, T, T, T, T, T, T, T, T, T, ...]
# 2의 배수 제거: [F, F, T, T, F, T, F, T, F, T, F, T, F, ...]
#
# e.g., n = 30, current = 3:
# 시작: [F, F, T, T, F, T, F, T, F, T, F, T, F, ...]
# 3의 배수 제거: [F, F, T, T, F, F, F, T, F, T, F, F, F, ...]
#
# 위와 같은 방식으로 모든 소수의 배수를 제거

def eratosthenes_sieve(n):
    # 초기 설정: 0과 1은 소수가 아니므로 False, 나머지는 모두 True로 설정
    sieve = [False, False] + [True for _ in range(2, n + 1)]
    primes = []

    for current in range(2, int(n**0.5) + 1):
        if sieve[current]:  # current가 소수인 경우
            for multiple in range(current * 2, n + 1, current):
                sieve[multiple] = False
                


    for i in range(current + 1, n + 1):
        if sieve[i]:
            primes.append(i)
    
    return primes

n = 30
print(eratosthenes_sieve(n))
