#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 에러 메시지: IndexError: list index out of range
# 의미: 리스트의 범위를 벗어나는 인덱스에 액세스하려고 할 때 발생합니다.

# 에러 발생 코드
my_list = [1, 2, 3]
print(my_list[3])

# 해결 방법:
# 리스트의 길이를 확인하고, 범위 내의 인덱스만 사용하여 오류를 방지할 수 있습니다.
# 예:
# if len(my_list) > 3:
#     print(my_list[3])
# else:
#     print("Index out of range")
