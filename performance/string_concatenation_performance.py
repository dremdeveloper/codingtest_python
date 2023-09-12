import time

num_elements = 1000000
strings = ["abcd"] * num_elements

# += 연산자 사용
start_time = time.time()
result_str = ""
for s in strings:
    result_str += s
plus_equals_time = time.time() - start_time

# join() 메서드 사용
start_time = time.time()
result_str = "".join(strings)
join_time = time.time() - start_time

print(f"Using += operator took: {plus_equals_time:.6f} seconds")# 0.514103초(환경 마다 다를 수 있음)
print(f"Using join() method took: {join_time:.6f} seconds")# 0.020838초(환경 마다 다를 수 있음)
