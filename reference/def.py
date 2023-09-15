#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# 파이썬에서 "def" 키워드는 함수를 정의할 때 사용됩니다. 
# 함수는 특정 작업을 수행하는 코드 블록입니다. 
# 함수는 인자를 받을 수도 있고, 결과를 반환할 수도 있습니다.

# 1. 인자가 없고 반환 값도 없는 함수:
def greet():
    print("Hello!")

# 함수 호출: greet()
# 출력: Hello!

# 2. 인자가 있는 함수:
def greet_person(name):
    print(f"Hello, {name}!")

# 함수 호출: greet_person("John")
# 출력: Hello, John!

# 3. 기본 인자가 있는 함수:
# 기본 인자는, 인자가 전달되지 않은 경우 사용되는 기본 값을 설정합니다.
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

# 함수 호출: greet_with_default()
# 출력: Hello, Guest!

# 4. 반환 값이 있는 함수:
# "return" 키워드를 사용하여 함수의 결과를 반환할 수 있습니다.
def add_numbers(a, b):
    return a + b

# 함수 호출: add_numbers(1, 2)
# 반환 값: 3

# 이제 각 함수를 호출해보며 그 결과를 확인해봅시다!
greet()
greet_person("John")
greet_with_default()
result = add_numbers(1, 2)
print(f"Result of addition: {result}")

# 위 코드에서는 다양한 유형의 함수를 "def" 키워드를 사용하여 정의했습니다.
# 함수의 인자와 반환 값에 대한 개념도 설명했습니다.
