#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# 파이썬에서, 객체는 뮤터블(mutable) 또는 이뮤터블(immutable) 두 가지 유형으로 나뉩니다.
# 뮤터블 객체는 객체가 생성된 후에도 그 상태를 변경할 수 있습니다. (예: 리스트, 딕셔너리)
# 이뮤터블 객체는 객체가 생성된 후에 그 상태를 변경할 수 없습니다. (예: 정수, 문자열, 튜플)

# 이뮤터블 예시: 문자열
immutable_example = "Hello, World!"
# immutable_example[0] = 'h'  # 이 줄은 에러를 일으킵니다, 문자열은 변경할 수 없습니다.

# 뮤터블 예시: 리스트
mutable_example = [1, 2, 3, 4]
mutable_example[0] = 0  # 리스트는 변경할 수 있습니다, 따라서 이 줄은 에러를 일으키지 않습니다.
print(mutable_example)  # 출력: [0, 2, 3, 4]

# 튜플 (이뮤터블) 와 리스트 (뮤터블)의 비교
tuple_example = (1, 2, 3)  # 튜플은 이뮤터블 객체입니다.
# tuple_example[0] = 0  # 이 줄은 에러를 일으킵니다, 튜플은 변경할 수 없습니다.

list_example = [1, 2, 3]  # 리스트는 뮤터블 객체입니다.
list_example[0] = 0  # 이 줄은 에러를 일으키지 않습니다, 리스트는 변경할 수 있습니다.
print(list_example)  # 출력: [0, 2, 3]
