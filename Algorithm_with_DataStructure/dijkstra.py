# 1. 알고리즘의 개념:
#    다익스트라 알고리즘은 그래프에서 한 노드로부터 다른 모든 노드까지의 최단 경로를 찾는 알고리즘이다.
#    이 알고리즘은 음수 가중치를 가진 간선을 허용하지 않는다.

# 2. 예시 입력 / 출력:
#    입력: 그래프의 노드 개수 V, 간선 정보 edges, 시작 노드 src
#    출력: 시작 노드로부터 각 노드까지의 최단 거리가 담긴 배열

# 3. 알고리즘의 시간 복잡도:
#    O((V+E)logV), 여기서 V는 노드의 수, E는 간선의 수

# 4. 해당 알고리즘으로 풀 수 있는 문제 예시:
#    - 한 지점에서 다른 지점까지의 최단 경로 찾기
#    - 네트워크 라우팅 알고리즘

from heapq import heappush, heappop

def dijkstra(V, edges, src):
    # 시작 노드에서 다른 모든 노드까지의 최단 거리를 담을 리스트 초기화
    distance = [float('inf')] * V
    distance[src] = 0

    # 그래프를 인접 리스트 형태로 변환
    graph = [[] for _ in range(V)]
    for u, v, w in edges:
        graph[u].append((v, w))

    # 우선순위 큐를 사용하여 현재 노드까지의 거리를 관리
    pq = [(0, src)]
    while pq:
        dist, node = heappop(pq)

        # 이미 처리된 노드는 무시
        if dist > distance[node]:
            continue

        # 현재 노드와 인접한 노드들의 거리 갱신
        for neighbor, weight in graph[node]:
            if dist + weight < distance[neighbor]:
                distance[neighbor] = dist + weight
                heappush(pq, (distance[neighbor], neighbor))

    return distance

# 간선 정보: (u, v, w) - u에서 v로 가는 가중치 w의 간선
edges = [(0, 1, 1), (1, 2, 3), (0, 2, 4), (1, 3, 2), (2, 3, -1)]

# 노드의 개수와 시작 노드 설정
V = 4
src = 0

# 다익스트라 알고리즘 실행 및 결과 출력
result = dijkstra(V, edges, src)
if result:
    print("노드로부터의 최단 거리:", result)
