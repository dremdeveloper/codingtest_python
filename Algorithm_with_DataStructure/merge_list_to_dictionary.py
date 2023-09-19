#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 리스트를 딕셔너리로 병합하는 알고리즘은 두 개의 리스트를 키와 값 쌍으로 갖는 딕셔너리로 병합하는 알고리즘입니다.
# Python에서는 dict 함수와 zip 함수를 이용하여 두 리스트를 딕셔너리로 병합할 수 있습니다.
# 주의할 점은 두 리스트의 길이가 동일해야 합니다.

def merge_list_to_dictionary(keys, values):
    return dict(zip(keys, values))

# 예시 사용법
keys = ["a", "b", "c"]
values = [1, 2, 3]
print(merge_list_to_dictionary(keys, values))  # 출력: {'a': 1, 'b': 2, 'c': 3}
