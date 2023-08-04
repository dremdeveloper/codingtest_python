from collections import defaultdict, deque

def solution(graph, start):
  # 그래프를 인접 리스트로 변환
  adj_list = defaultdict(list)
  for u, v in graph:
    adj_list[u].append(v)

  # BFS 탐색 함수
  def bfs(start):
    visited = set()  # ❶ 방문한 노드를 저장할 셋
    queue = deque([start])  # ❷ 탐색시 맨 처음 방문할 노드 푸시
    while queue:  # ❸ 큐가 비어있지 않은 동안 반복
      node = queue.popleft()  # ❹ 큐에 있는 원소 중 가장 먼저 푸시된 원소 팝
      if node not in visited:  # ❺ 방문하지 않은 노드인 경우
        visited.add(node)  # ❻ 현재노드를 방문한 노드로 추가
        result.append(node)  # ❼ 현재 노드를 결과리스트에 추가
        for neighbor in adj_list.get(node, []):  # ❽ 인접한 이웃 노드들에 대해서
          if neighbor not in visited:  # ➒ 방문되지 않은 이웃 노드인 경우
            queue.append(neighbor)

  result = []
  bfs(start)  # ➓ 시작 노드부터 BFS 탐색 수행
  return result
