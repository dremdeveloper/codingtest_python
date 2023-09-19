#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 에러 메시지: KeyError: 'key'
# 의미: 딕셔너리에서 존재하지 않는 키를 참조하려고 할 때 발생하는 에러입니다.

# 에러 발생 코드
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])

# 해결 방법:
# 딕셔너리에 키가 있는지 확인하거나 try-except 블록을 사용하여 에러를 처리합니다.
# 예:
# if 'c' in my_dict:
#     print(my_dict['c'])
# else:
#     print("Key not found")
