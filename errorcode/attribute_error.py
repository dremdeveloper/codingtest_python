#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 에러 메시지: AttributeError: 'list' object has no attribute 'size'
# 의미: 객체에 없는 속성이나 메서드를 호출하려고 할 때 발생하는 에러입니다.

# 에러 발생 코드
my_list = [1, 2, 3]
print(my_list.size())

# 해결 방법:
# 올바른 메서드나 속성 이름을 사용하거나, 해당 객체 타입에 적합한 메서드/속성을 사용합니다.
# 예:
# print(len(my_list))  # 리스트의 길이를 얻으려면 len 함수를 사용합니다.
