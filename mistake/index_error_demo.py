#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 예시 리스트 생성
my_list = [10, 20, 30, 40, 50]

# 실수 예: 리스트의 길이를 넘는 인덱스에 접근하려고 할 때
# print(my_list[5])  # IndexError: list index out of range

# 파이썬에서 리스트의 인덱스는 0부터 시작하므로 my_list[5]는 유효하지 않습니다.

# 실수 예: 음수 인덱스를 사용하되 범위를 벗어나는 경우
# print(my_list[-6])  # IndexError: list index out of range

# 파이썬에서 음수 인덱스는 리스트의 끝에서부터 시작하여 역순으로 원소에 접근합니다.
# -1은 마지막 원소, -2는 끝에서 두 번째 원소를 가리킵니다. 그러나 -6은 범위를 벗어납니다.

# 올바른 사용법: 인덱스의 유효성을 확인한 후 접근
index_to_access = 4
if 0 <= index_to_access < len(my_list):
    print(my_list[index_to_access])  # 올바르게 50을 출력합니다.

# 음수 인덱스 사용 시 올바른 사용법:
negative_index = -2
if -len(my_list) <= negative_index < 0:
    print(my_list[negative_index])  # 올바르게 40을 출력합니다.

# 문자열에서도 마찬가지로 인덱스 범위를 벗어나면 에러가 발생합니다.
# string_example = "hello"
# print(string_example[10])  # IndexError: string index out of range
