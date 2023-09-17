#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 벨만-포드 알고리즘(Bellman-Ford Algorithm) 예제 코드
# 1. 알고리즘의 개념: 
#    벨만-포드 알고리즘은 그래프에서 주어진 시작 노드로부터 다른 모든 노드까지의 최단 경로를 찾는 알고리즘이다.
#    음수 가중치를 가진 간선도 처리할 수 있으나, 음수 사이클이 있는 경우에는 알고리즘이 작동하지 않는다.

# 2. 예시 입력 / 출력: 
#    입력: 그래프의 노드 개수 V, 간선 정보 edges, 시작 노드 src
#    출력: 시작 노드로부터 각 노드까지의 최단 거리가 담긴 배열

# 3. 알고리즘의 시간 복잡도: 
#    O(V*E), 여기서 V는 노드의 수이고, E는 간선의 수이다.

# 4. 해당 알고리즘으로 풀 수 있는 문제 예시:
#    - 그래프에서 단일 출발점 최단 경로 문제
#    - 음수 가중치가 있는 그래프에서의 최단 경로 문제 (단, 음수 사이클이 없어야 함)

def bellman_ford(V, edges, src):
    # 시작 노드에서 다른 모든 노드까지의 최단 거리를 담을 리스트 초기화
    distance = [float('inf')] * V
    distance[src] = 0

    # 모든 간선에 대해 V-1번 반복하여 최단 거리를 갱신
    for _ in range(V-1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # 음수 사이클 체크: 한 번 더 반복하여 거리가 갱신되면 음수 사이클이 존재함
    for u, v, w in edges:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            print("그래프에 음수 사이클이 존재합니다.")
            return None

    return distance

# 간선 정보 (u, v, w) - u에서 v로 가는 가중치 w의 간선
edges = [(0, 1, 1), (1, 2, 3), (0, 2, 4), (1, 3, 2), (2, 3, -1)]

# 노드의 개수와 시작 노드 설정
V = 4
src = 0

# 벨만-포드 알고리즘 실행 및 결과 출력
result = bellman_ford(V, edges, src)
if result:
    print("노드로부터의 최단 거리:", result)
