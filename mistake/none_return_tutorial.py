#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 파이썬에서 return 문장이 없는 함수 정의
def no_return_function():
    print("This function doesn't have a return statement.")

# 함수를 호출
result = no_return_function()  
print(result)  # None이 출력됩니다.

# 파이썬에서 함수가 명시적으로 값을 반환하지 않으면, 기본적으로 None을 반환합니다.

# 실수 예: 반환 값이 있는 것처럼 함수를 사용하려고 할 때
def add(a, b):
    result = a + b
    # 여기서 return을 깜빡하고 쓰지 않았습니다.

sum_result = add(5, 3)
# print(sum_result + 2)  
# 위의 코드는 TypeError를 발생시킵니다. 왜냐하면 sum_result는 None이기 때문입니다.

# 올바른 사용법: 함수에서 값을 반환하려면 return 문을 사용해야 합니다.
def correct_add(a, b):
    return a + b

correct_sum_result = correct_add(5, 3)
print(correct_sum_result + 2)  # 올바르게 10이 출력됩니다.

# 때로는 함수가 None을 반환하는 것이 의도된 것일 수 있습니다. 
# 그러나 함수의 반환 값을 사용하려고 할 때는 항상 반환 값이 None인지 아닌지 확인하는 것이 좋습니다.
