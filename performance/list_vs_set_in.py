#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. 리스트에서 in 테스트: 리스트에서 'in' 연산자를 사용하여 요소가 있는지 확인하는 것은 선형 시간 복잡도를 가지며, 
#    즉, 시간 복잡도는 O(n)입니다. 리스트에서는 각 요소를 처음부터 순차적으로 탐색하여 검색 값이 있는지 확인합니다.
#
# 2. 집합에서 in 테스트: 반면에, 집합(set)에서 'in' 연산자를 사용하면, 일반적으로 상수 시간 복잡도 O(1)으로 요소를 찾을 수 있습니다. 
#    이는 집합이 해시 테이블 기반의 자료구조이기 때문에, 요소의 해시 값을 사용하여 빠르게 해당 요소를 찾을 수 있습니다.
import time

# 데이터 준비
num_elements = 1000000
test_value = num_elements + 1  # 이 값은 리스트와 집합에 없음.

lst = list(range(num_elements))
s = set(lst)

# 리스트에서 in 테스트
start_time = time.time()
result_list = test_value in lst
end_time = time.time()
list_time = end_time - start_time

# 집합에서 in 테스트
start_time = time.time()
result_set = test_value in s
end_time = time.time()
set_time = end_time - start_time

print(f"List membership test took: {list_time:.6f} seconds")# 0.019357초(환경마다 다를 수 있음)
print(f"Set membership test took: {set_time:.6f} seconds")# 0.000003초(환경마다 다를 수 있음)
