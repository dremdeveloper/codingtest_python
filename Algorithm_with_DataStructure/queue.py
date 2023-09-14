from collections import deque

queue = deque( )

# 큐에 데이터 추가
queue.append(1)
queue.append(2)
queue.append(3)

# 큐의 맨 앞 데이터 제거
first_item = queue.popleft( )
print(first_item) # 1

# 큐에 데이터 추가
queue.append(4)
queue.append(5)

# 큐의 맨 앞 데이터 제거
first_item = queue.popleft( )
print(first_item) # 2