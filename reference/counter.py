from collections import Counter

# Counter(iterable)
# iterable 객체(예: 문자열, 리스트, 튜플 등)를 받아, 각 요소의 출현 횟수를 계산하여 Counter 객체를 생성
# 시간 복잡도: O(n), 여기서 n은 iterable의 길이
iterable_example = 'abracadabra'
counter_obj = Counter(iterable_example)
print(counter_obj)
# 출력값: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Counter.most_common(num)
# Counter 객체에서 가장 빈번하게 발생하는 num 개의 요소와 그 개수를 리스트로 반환
# num이 지정되지 않거나 None이면 모든 요소를 반환
# 시간 복잡도: O(n log n), 여기서 n은 Counter 객체의 원수 개수
most_common_elements = counter_obj.most_common(2)
print(most_common_elements)
# 출력값: [('a', 5), ('b', 2)]

# Counter.elements()
# Counter 객체에서 요소들을 횟수에 따라 반복하는 이터레이터를 반환.
# 시간 복잡도: O(n), 여기서 n은 elements의 총 개수.
elements_iterator = counter_obj.elements()
print(list(elements_iterator))
# 출력값: ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']
