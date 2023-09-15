#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# 함수의 합성(Composition of functions)은 하나의 함수의 출력이 또 다른 함수의 입력으로 사용되는 것입니다.
# 이를 통해 여러 함수를 결합하여 더 복잡한 기능을 수행할 수 있습니다.
# Python에서는 이러한 함수 합성을 쉽게 구현할 수 있습니다.

# 먼저, 두 개의 간단한 함수를 정의해봅시다.
def double(x):
    return x * 2

def increment(x):
    return x + 1

# 이제, 이 두 함수를 합성하는 새로운 함수를 정의할 수 있습니다.
def composition_function(x):
    return increment(double(x))  # double 함수의 출력이 increment 함수의 입력으로 사용됩니다.

# 함수 호출 예제
result = composition_function(5)  # 먼저 5를 2배로 만든 후, 1을 더합니다. 따라서 결과는 11입니다.
print(result)  # 출력: 11
