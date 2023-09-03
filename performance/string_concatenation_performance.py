import time

num_elements = 1000000
strings = ["a"] * num_elements

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

print(f"Using += operator took: {plus_equals_time:.6f} seconds")
print(f"Using join() method took: {join_time:.6f} seconds")
