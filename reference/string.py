#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# str1 + str2: 두 문자열 str1과 str2를 연결합니다.
# 반환값: 새로운 문자열
# 시간 복잡도: O(n + m), n과 m은 각각 str1과 str2의 길이입니다.
str1 = "Hello"
str2 = " World"
result = str1 + str2
print(result)  # 출력: "Hello World"

# delimiter.join(list_of_strings): delimiter 문자열을 사용하여 list_of_strings의 모든 문자열을 연결합니다.
# 반환값: 새로운 문자열
# 시간 복잡도: O(n), n은 list_of_strings의 모든 문자열 길이의 합입니다.
delimiter = " | "
list_of_strings = ["apple", "banana", "cherry"]
result = delimiter.join(list_of_strings)
print(result)  # 출력: "apple | banana | cherry"

# str.replace(old, new): 문자열 str에서 old 부분 문자열을 new 부분 문자열로 교체합니다.
# 반환값: 새로운 문자열
# 시간 복잡도: O(n), n은 str의 길이입니다.
str3 = "Hello, World!"
result = str3.replace("World", "Python")
print(result)  # 출력: "Hello, Python!"

# str.split(sep): 문자열 str을 sep 문자열을 기준으로 나눕니다.
# 반환값: 문자열 리스트
# 시간 복잡도: O(n), n은 str의 길이입니다.
str4 = "apple,banana,cherry"
result = str4.split(",")
print(result)  # 출력: ['apple', 'banana', 'cherry']

# str.startswith(prefix): 문자열 str이 prefix로 시작하는지 확인합니다.
# 반환값: bool (True 또는 False)
# 시간 복잡도: O(k), k는 prefix의 길이입니다.
str5 = "Hello, World!"
result = str5.startswith("Hello")
print(result)  # 출력: True

# str.endswith(suffix): 문자열 str이 suffix로 끝나는지 확인합니다.
# 반환값: bool (True 또는 False)
# 시간 복잡도: O(k), k는 suffix의 길이입니다.
result = str5.endswith("World!")
print(result)  # 출력: True
