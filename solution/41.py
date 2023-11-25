def solution(graph, source):
  # ➊ 그래프의 노드 수
  num_vertices = len(graph)

  # ➋ 거리 배열 초기화
  distance = [float("inf")] * num_vertices
  distance[source] = 0

  # ➌ 직전 경로 배열 초기화
  predecessor = [None] * num_vertices

  # ➍ 간선 수 만큼 반복하여 최단 경로 갱신
  for temp in range(num_vertices - 1):
    for u in range(num_vertices):
      for v, weight in graph[u]:
        # ➎ 현재 노드 u를 거쳐서 노드 v로 가는 경로의 거리가 기존에 저장된 노드 v까지의 거리보다 짧은 경우
        if distance[u] + weight < distance[v]:
          # ➏ 최단 거리를 갱신해줍니다.
          distance[v] = distance[u] + weight
          # ➐ 직전 경로를 업데이트합니다.
          predecessor[v] = u

  # ➑ 음의 가중치 순회 체크
  for u in range(num_vertices):
    for v, weight in graph[u]:
      # ➒ 현재 노드 u를 거쳐서 노드 v로 가는 경로의 거리가 기존에 저장된 노드 v까지의 거리보다 짧은 경우
      if distance[u] + weight < distance[v]:
        # ❿ 음의 가중치 순회가 발견되었으므로 [-1]을 반환합니다.
        return [-1]
  return [distance, predecessor]

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([[(1, 4), (2, 3), (4, -6 )], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)],[(2, 2)]],0)) #반환갑 : [[0, -2, -4, 3, -6], [None, 2, 4, 1, 0]]
# print(solution([[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]],0)) # 반환값 : [-1]
