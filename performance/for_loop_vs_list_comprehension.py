#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. for 루프 사용: 이 부분에서는 for 루프를 사용하여 각 숫자의 제곱을 계산하고, 이를 squared_numbers 리스트에 하나씩 추가합니다. 
#    이 과정에서 반복문을 통해 반복적인 메서드 호출이 발생하며, 일반적으로 시간 복잡도는 O(n)입니다.
#
# 2. list comprehension 사용: list comprehension은 for 루프를 사용하는 것보다 더 빠른 방법으로 리스트를 생성할 수 있습니다. 
#    이는 내부적으로 최적화가 더 잘 되어 있어 연산이 더 빠르게 진행되기 때문입니다. 
#    이 방법 역시 시간 복잡도는 O(n)이지만, 상수 시간 요소가 for 루프보다 작아 성능이 더 좋습니다.
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

print(f"Using for loop took: {for_loop_time:.6f} seconds") # 1.347505초(환경마다 다를 수 있음)
print(f"Using list comprehension took: {list_comprehension_time:.6f} seconds") # 0.536171초(환경마다 다를 수 있음)
