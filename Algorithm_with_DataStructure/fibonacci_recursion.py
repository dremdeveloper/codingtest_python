#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. 알고리즘의 개념:
#    피보나치 수열은 첫 번째와 두 번째 항이 1이고, 그 이후의 항은 직전의 두 항의 합인 수열입니다.
#    이 함수는 재귀적 방법으로 피보나치 수열의 n 번째 항을 계산합니다.
   
# 2. 예시 입력 / 출력:
#    입력: 5
#    출력: 5 (피보나치 수열의 5번째 항은 5입니다)
   
# 3. 알고리즘의 시간 복잡도:
#    이 알고리즘의 시간 복잡도는 O(2^n)입니다. 이는 각 호출이 두 개의 새로운 호출을 생성하기 때문에 호출 횟수가 exponential하게 증가합니다.
   
# 4. 해당 알고리즘으로 풀 수 있는 문제 예시:
#    - n 번째 피보나치 수 찾기
#    - 피보나치 수열을 사용하여 복잡한 수학적 문제 해결
   
# 5. 상세 과정:
#    - n이 0이나 1인 경우, n을 반환합니다. (기저 사례)
#    - 그렇지 않으면, fibonacci(n-1)과 fibonacci(n-2)를 재귀적으로 호출하여 두 결과를 합칩니다.
   
# 호출 구조는 다음과 같습니다 (n=5의 경우):
# 
#     fibonacci(5)
#     ├─ fibonacci(4)
#     │  ├─ fibonacci(3)
#     │  │  ├─ fibonacci(2)
#     │  │  │  ├─ fibonacci(1)
#     │  │  │  └─ fibonacci(0)
#     │  │  └─ fibonacci(1)
#     │  └─ fibonacci(2)
#     │     ├─ fibonacci(1)
#     │     └─ fibonacci(0)
#     └─ fibonacci(3)
#        ├─ fibonacci(2)
#        │  ├─ fibonacci(1)
#        │  └─ fibonacci(0)
#        └─ fibonacci(1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
       
# 예제:
print(fibonacci(5))  # 출력: 5
