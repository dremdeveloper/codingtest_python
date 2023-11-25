from collections import defaultdict

def solution(graph, start):
  # ❶ 그래프를 인접 리스트로 변환
  adj_list = defaultdict(list)
  for u, v in graph:
    adj_list[u].append(v)

  # ❷ DFS 탐색 함수
  def dfs(node, visited, result):
    visited.add(node)  # ❸ 현재 노드를 방문한 노드들의 집합에 추가
    result.append(node)  # ❹ 현재 노드를 결과 리스트에 추가
    for neighbor in adj_list.get(node, []):  # ❺ 현재 노드와 인접한 노드순회
      if neighbor not in visited:  # ❻ 아직 방문하지 않은 노드라면
        dfs(neighbor, visited, result)

  # DFS를 순회한 결과를 반환
  visited = set()
  result = []
  dfs(start, visited, result)  # ❼ 시작 노드에서 깊이 우선 탐색 시작
  return result  # ❽ DFS 탐색 결과 반환

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A')) # 반환값 : ['A', 'B', 'C', 'D', 'E']
# print(solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A')) # 반환값 : ['A', 'B', 'D', 'E', 'F', 'C']
