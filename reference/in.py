#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# 파이썬에서 "in" 연산자는 주로 시퀀스(리스트, 튜플, 문자열 등)에 어떤 요소가 포함되어 있는지 검사할 때 사용됩니다. 
# 또한 "in" 연산자는 반복문에서도 사용되며, 이 경우 시퀀스의 각 요소를 순회합니다.
# "in" 연산자의 사용은 코드를 간결하고 읽기 쉽게 만들어 줍니다.

# 예시 1: 리스트에서 "in" 연산자 사용
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # 출력: True (3이 리스트에 있으므로)
print(6 in my_list)  # 출력: False (6이 리스트에 없으므로)

# 예시 2: 문자열에서 "in" 연산자 사용
my_string = "Hello, Python!"
print('Python' in my_string)  # 출력: True ('Python'이 문자열에 포함되어 있으므로)
print('Java' in my_string)  # 출력: False ('Java'는 문자열에 포함되어 있지 않으므로)

# 예시 3: 딕셔너리에서 "in" 연산자 사용 (키 검사)
my_dict = {'a': 1, 'b': 2, 'c': 3}
print('a' in my_dict)  # 출력: True ('a'가 딕셔너리의 키 중 하나이므로)
print('d' in my_dict)  # 출력: False ('d'는 딕셔너리의 키 중 하나가 아니므로)

# 예시 4: for 루프에서 "in" 연산자 사용
for i in range(5):  # 0부터 4까지의 범위에서 각 요소에 대해
    print(i)  # 출력: 0, 1, 2, 3, 4 (한 줄에 하나씩)

# "in" 연산자는 코드를 간단하고 직관적으로 만들며, 다양한 데이터 타입에서 요소의 존재를 검사할 때 유용합니다.
