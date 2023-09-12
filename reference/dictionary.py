# dic.get(key)
# 딕셔너리 dic에서 주어진 key에 해당하는 값을 반환합니다. 
# key가 딕셔너리에 없으면 None을 반환합니다.
# 시간 복잡도: O(1)
dic = {'a': 1, 'b': 2, 'c': 3}
value = dic.get('a')
print(value)  # 출력값: 1
value = dic.get('d')
print(value)  # 출력값: None

# dic[key]
# 딕셔너리 dic에서 주어진 key에 해당하는 값을 반환합니다. 
# key가 딕셔너리에 없으면 KeyError를 발생시킵니다.
# 시간 복잡도: O(1)
try:
    value = dic['b']
    print(value)  # 출력값: 2
    value = dic['d']
    print(value)  # 출력값: (이 줄은 실행되지 않습니다; KeyError 발생)
except KeyError as e:
    print(e)  # 출력값: 'd'

# dic.pop(key)
# 딕셔너리 dic에서 주어진 key에 해당하는 항목을 제거하고 그 값을 반환합니다. 
# key가 딕셔너리에 없으면 KeyError를 발생시킵니다.
# 시간 복잡도: O(1)
try:
    value = dic.pop('c')
    print(value)  # 출력값: 3
    value = dic.pop('d')
    print(value)  # 출력값: (이 줄은 실행되지 않습니다; KeyError 발생)
except KeyError as e:
    print(e)  # 출력값: 'd'

# key in dic
# 주어진 key가 딕셔너리 dic에 있는지를 검사합니다. 
# 시간 복잡도: O(1)
key_presence = 'a' in dic
print(key_presence)  # 출력값: True
key_presence = 'd' in dic
print(key_presence)  # 출력값: False
