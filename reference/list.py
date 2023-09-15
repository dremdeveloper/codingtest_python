#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

lst = [1, 2, 3, 4]

# append(item): 리스트의 끝에 item을 추가합니다. 반환값은 없습니다.
# 시간 복잡도: O(1) (상수 시간)
lst.append(5)
print(lst)  # 출력: [1, 2, 3, 4, 5]

# insert(idx, item): idx 위치에 item을 추가합니다. 반환값은 없습니다.
# 시간 복잡도: O(n) (n: 리스트의 길이)
lst.insert(2, 6)
print(lst)  # 출력: [1, 2, 6, 3, 4, 5]

# pop(): 리스트의 마지막 요소를 제거하고 반환합니다.
# 시간 복잡도: O(1) (상수 시간)
print(lst.pop())  # 출력: 5
print(lst)  # 출력: [1, 2, 6, 3, 4]

# pop(0): 리스트의 첫 번째 요소를 제거하고 반환합니다.
# 시간 복잡도: O(n) (n: 리스트의 길이)
print(lst.pop(0))  # 출력: 1
print(lst)  # 출력: [2, 6, 3, 4]

# remove(item): 리스트에서 item을 찾아 제거합니다. 반환값은 없습니다.
# 시간 복잡도: O(n) (n: 리스트의 길이)
lst.remove(6)
print(lst)  # 출력: [2, 3, 4]

# extend(s): 리스트에 s의 모든 요소를 추가합니다. 반환값은 없습니다.
# 시간 복잡도: O(k) (k: 추가하는 리스트 s의 길이)
lst.extend([7, 8])
print(lst)  # 출력: [2, 3, 4, 7, 8]

# lst[K]: 리스트의 K 위치의 요소에 접근합니다.
# 시간 복잡도: O(1) (상수 시간)
print(lst[2])  # 출력: 4

# lst1 + lst2: 두 리스트를 결합하여 새 리스트를 생성하고 반환합니다.
# 시간 복잡도: O(n+m) (n: lst1의 길이, m: lst2의 길이)
print([1, 2, 3] + [4, 5, 6])  # 출력: [1, 2, 3, 4, 5, 6]

# list(set): 집합을 리스트로 변환하여 중복을 제거합니다. 순서는 보장되지 않습니다.
# 시간 복잡도: O(n) (n: 리스트/집합의 길이)
print(list(set([1, 2, 2, 3, 3, 4])))  # 출력 : [1,2,3,4]

# item in lst: 리스트에 item이 있는지 확인합니다.
# 시간 복잡도: O(n) (n: 리스트의 길이)
print(3 in lst)  # 출력: True
