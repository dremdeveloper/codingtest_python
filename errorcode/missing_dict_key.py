#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 에러 메시지: KeyError: 'missing_key'
# 의미: 사전에서 존재하지 않는 키를 사용하여 값을 검색하려고 할 때 발생합니다.

# 에러 발생 코드
my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict["missing_key"])

# 해결 방법:
# 사전에 키가 있는지 확인하는 'in' 연산자를 사용하여 오류를 방지할 수 있습니다.
# 예:
# if "missing_key" in my_dict:
#     print(my_dict["missing_key"])
# else:
#     print("Key not found in the dictionary")
