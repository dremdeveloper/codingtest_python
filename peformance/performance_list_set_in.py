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

print(f"List membership test took: {list_time:.6f} seconds")
print(f"Set membership test took: {set_time:.6f} seconds")
