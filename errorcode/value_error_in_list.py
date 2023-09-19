#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 에러 메시지: ValueError: 'x' is not in list
# 의미: 리스트에서 존재하지 않는 요소를 remove 메소드를 사용하여 삭제하려 할 때 발생하는 에러입니다.

# 에러 발생 코드
my_list = [1, 2, 3]
my_list.remove('x')

# 해결 방법:
# 요소가 리스트에 있는지 확인하거나 try-except 블록을 사용하여 에러를 처리합니다.
# 예:
# if 'x' in my_list:
#     my_list.remove('x')
# else:
#     print("Value not found in the list")
