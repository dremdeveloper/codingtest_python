#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. 알고리즘의 개념:
#    BFS(너비 우선 탐색)는 그래프나 트리를 탐색하는 알고리즘 중 하나로,
#    루트 노드(혹은 다른 임의의 노드)에서 시작하여 인접한 노드들을 먼저 탐색하는 알고리즘입니다.
#    큐(Queue)를 사용하여 구현할 수 있으며, 아래 코드는 큐를 사용한 방법으로 BFS를 구현한 예입니다.

# 2. 예시 입력 / 출력:
#    입력: graph = {1: [2, 3], 2: [4, 5], 3: [], 4: [], 5: []}, start_node = 1
#    출력: [1, 2, 3, 4, 5]

# 3. 알고리즘의 시간 복잡도:
#    O(V + E) (V: 정점의 개수, E: 간선의 개수)

# 4. 해당 알고리즘으로 풀 수 있는 문제 예시:
#    - 최단 경로 찾기
#    - 그래프의 연결성분 찾기

# 5. BFS 상세 과정:
#    - 시작 노드(1)를 큐에 넣고, 방문 처리를 한다.
#    - 큐에서 노드를 하나 꺼낸다(노드 1).
#    - 해당 노드의 인접 노드 중 방문하지 않은 노드들(노드 2와 3)을 큐에 넣고 방문 처리를 한다.
#    - 큐에서 노드를 하나 꺼낸다(노드 2).
#    - 노드 2의 인접 노드 중 방문하지 않은 노드들(노드 4와 5)을 큐에 넣고 방문 처리를 한다.
#    - 위 과정을 큐가 빌 때까지 반복한다.

from collections import deque

def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    
    return visited

# 그래프를 인접 리스트로 표현
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

# BFS 알고리즘 실행
result = bfs(graph, 1)
print(result)
# 출력: [1, 2, 3, 4, 5]
