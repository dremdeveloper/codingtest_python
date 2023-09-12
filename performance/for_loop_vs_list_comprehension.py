import time

num_elements = 10000000

# for 루프 사용
start_time = time.time()
squared_numbers = []
for i in range(num_elements):
    squared_numbers.append(i * i)
for_loop_time = time.time() - start_time

# list comprehension 사용
start_time = time.time()
squared_numbers_comprehension = [i * i for i in range(num_elements)]
list_comprehension_time = time.time() - start_time

print(f"Using for loop took: {for_loop_time:.6f} seconds") # 1.347505(환경마다 다를 수 있음)
print(f"Using list comprehension took: {list_comprehension_time:.6f} seconds") # 0.536171초(환경마다 다를 수 있음)
