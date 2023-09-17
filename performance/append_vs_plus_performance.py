#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# append() 메서드와 + 연산자의 동작 및 시간 복잡도에 대한 설명:
# 1. append() 메서드: 리스트의 끝에 새 요소를 추가하는 연산으로, 시간 복잡도는 O(1)이며, 상수 시간이 걸립니다. 
#    리스트의 크기와 무관하게 일정한 시간이 소요됩니다.
# 2. + 연산자: 두 리스트를 합치는 연산으로, 시간 복잡도는 O(n)입니다. 리스트의 크기에 비례하여 시간이 걸리며, 
#    반복문 안에서 사용할 경우 각 반복마다 새 리스트를 생성해야 하므로 시간 소요가 큽니다.
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

print(f"Using append() took: {append_time:.6f} seconds")# 0.002196초(환경마다 다를 수 있음)
print(f"Using + operator took: {plus_time:.6f} seconds")# 0.297017초(환경마다 다를 수 있음)
