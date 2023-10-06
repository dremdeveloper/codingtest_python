#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 파이썬 리스트는 0-based 인덱싱을 사용합니다.
# 즉, 첫 번째 원소의 인덱스는 0입니다.
my_list = [10, 20, 30, 40, 50]

# 0-based 인덱싱 사용
print(my_list[0])  # 첫 번째 원소 10을 출력합니다.

# 실수 예: 1-based 인덱싱을 생각하고 코드를 작성할 경우
# 아래 코드는 두 번째 원소 20을 출력합니다.
# print(my_list[1])

# 만약 문제가 1-based 인덱싱을 기준으로 제시된 경우,
# 올바른 인덱스에 접근하기 위해서는 인덱스에서 1을 빼야 합니다.
index_in_1_based = 1
correct_index_in_0_based = index_in_1_based - 1
print(my_list[correct_index_in_0_based])  # 올바르게 첫 번째 원소 10을 출력합니다.

# 문자열도 0-based 인덱싱을 사용합니다.
my_string = "hello"
print(my_string[0])  # 첫 번째 문자 'h'를 출력합니다.

# 실수 예: 문자열에서 1-based 인덱싱을 사용하려 할 경우
# 아래 코드는 두 번째 문자 'e'를 출력합니다.
# print(my_string[1])

# 마찬가지로, 문제가 1-based 인덱싱을 기준으로 제시된 경우에도 인덱스에서 1을 빼야 합니다.
index_in_1_based_str = 1
correct_index_in_0_based_str = index_in_1_based_str - 1
print(my_string[correct_index_in_0_based_str])  # 올바르게 첫 번째 문자 'h'를 출력합니다.
