#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 전역 변수 (global variable): 프로그램의 모든 부분에서 접근 가능한 변수
global_variable = "I'm a global variable"

def function_example():
    # 지역 변수 (local variable): 함수 내에서만 접근 가능한 변수
    local_variable = "I'm a local variable"

    # 전역 변수를 함수 내에서 사용하려면 global 키워드를 사용해야 합니다.
    global global_variable
    print(global_variable)  # 올바른 방법으로 전역 변수를 출력합니다.

    # 실수 예: 지역 변수와 전역 변수의 이름이 같을 경우
    # 아래의 코드는 새로운 지역 변수를 만들고, 전역 변수는 변경되지 않습니다.
    global_variable = "I'm a changed local variable"
    print(global_variable)  # "I'm a changed local variable"을 출력합니다.

function_example()

# 여전히 원래의 값인 "I'm a global variable"을 출력합니다.
# 왜냐하면 위의 함수 내에서는 지역 변수만 변경되었기 때문입니다.
print(global_variable)

# 올바른 방법으로 전역 변수를 변경하려면:
def change_global_variable():
    global global_variable  # 전역 변수를 사용하겠다는 것을 명시적으로 선언합니다.
    global_variable = "I'm a changed global variable"

change_global_variable()
print(global_variable)  # "I'm a changed global variable"을 출력합니다.

# 실수 예: 지역 변수를 함수 외부에서 사용하려고 할 때
# 아래 코드는 에러를 발생시킵니다. 왜냐하면 local_variable은 function_example 함수 내의 지역 변수이기 때문입니다.
# print(local_variable)

# 올바른 방법은 해당 지역 변수를 함수 내에서만 사용하거나, 필요한 경우 전역 변수로 변경하는 것입니다.
