def solution(n, wires):
  # ➊ 그래프 생성
  graph = [[] for _ in range(n + 1)]
  for a, b in wires:
    graph[a].append(b)
    graph[b].append(a)

  # ➋ 깊이 우선 탐색 함수
  def dfs(node, parent):
    cnt = 1
    for child in graph[node]:  # ➌ 현재 노드의 자식 노드들에 방문
      if child != parent:  # ➍ 부모 노드가 아닌 경우에만 탐색
        cnt += dfs(child, node)
    return cnt

  min_diff = float("inf")
  for a, b in wires:
    # ➎ 간선 제거
    graph[a].remove(b)
    graph[b].remove(a)

    # ➏ 각 전력망 송전탑 개수 계산
    cnt_a = dfs(a, b)
    cnt_b = n - cnt_a

    # ➐ 최소값 갱신
    min_diff = min(min_diff, abs(cnt_a - cnt_b))

    # ➑ 간선 복원
    graph[a].append(b)
    graph[b].append(a)

  return min_diff
