#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. += 연산자 사용: 이 부분에서는 문자열 결합을 위해 += 연산자를 사용합니다. 문자열은 변경이 불가능한 객체이므로, 
#    매번 += 연산을 수행할 때마다 새로운 문자열 객체가 생성되고, 이전 문자열의 내용과 새로운 문자열의 내용이 복사됩니다.
#    이로 인해 이 연산은 시간 복잡도 O(n^2)를 가지게 됩니다.
#
# 2. join() 메서드 사용: join() 메서드는 문자열 리스트를 한 번에 결합하는 방법을 제공합니다. 
#    이 메서드는 내부적으로 더 효율적인 메모리 관리를 하며, 문자열을 한 번에 합치기 때문에 시간 복잡도 O(n)을 가집니다. 
#    따라서, 큰 문자열 리스트에서는 join() 메서드가 += 연산자보다 훨씬 빠른 성능을 보여줍니다.

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
