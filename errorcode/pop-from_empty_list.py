#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 에러 메시지: IndexError: pop from empty list
# 의미: 비어 있는 리스트에서 요소를 pop(제거)하려고 할 때 발생합니다.

# 에러 발생 코드
my_list = []
my_list.pop()

# 해결 방법:
# 리스트가 비어 있지 않은지 확인하여 오류를 방지할 수 있습니다.
# 예:
# if my_list:
#     my_list.pop()
# else:
#     print("Cannot pop from an empty list")
