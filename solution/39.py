from collections import defaultdict, deque

def solution(graph, start):
  # 그래프를 인접 리스트로 변환
  adj_list = defaultdict(list)
  for u, v in graph:
    adj_list[u].append(v)
    
  # BFS 탐색 함수
  def bfs(start):
    visited = set()  # ❶ 방문한 노드를 저장할 셋
    
    # ❷ 탐색시 맨 처음 방문할 노드 푸시 하고 방문처리
    queue = deque([start])  
    visited.add(start)  
    result.append(start)  
    
    # ❸ 큐가 비어있지 않은 동안 반복
    while queue:  
      node = queue.popleft()  # ❹ 큐에 있는 원소 중 가장 먼저 푸시된 원소 팝
      for neighbor in adj_list.get(node, []):  #❺  인접한 이웃 노드들에 대해서
        if neighbor not in visited:  # ❻ 방문되지 않은 이웃 노드인 경우
            # ❼ 이웃노드를 방문 처리함
            queue.append(neighbor)
            visited.add(neighbor)  
            result.append(neighbor)

  result = []
  bfs(start)  # ❽ 시작 노드부터 BFS 탐색 수행
  return result

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)],1)) # 반환값 :[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)],1)) # 반환값 : [1, 2, 3, 4, 5, 0]
 
