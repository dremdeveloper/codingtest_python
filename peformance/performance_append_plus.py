import time

num_elements = 10000

# append() 사용
start_time = time.time()
lst_append = []
for i in range(num_elements):
    lst_append.append(i)
append_time = time.time() - start_time

# + 연산자 사용
start_time = time.time()
lst_plus = []
for i in range(num_elements):
    lst_plus = lst_plus + [i]
plus_time = time.time() - start_time

print(f"Using append() took: {append_time:.6f} seconds")
print(f"Using + operator took: {plus_time:.6f} seconds")
