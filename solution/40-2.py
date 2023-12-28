import heapq

def solution(graph, start):
    distances = {node: float("inf") for node in graph}  # 모든 노드의 거리 값을 무한대로 초기화
    distances[start] = 0  # 시작 노드의 거리 값은 0으로 초기화
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드를 큐에 삽입
    paths = {start: [start]}  # 시작 노드의 경로를 초기화
    visited = set()  # 방문한 노드를 저장할 집합

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node in visited:  # 이미 방문한 노드는 무시
            continue
        visited.add(current_node)  # 현재 노드를 방문한 노드 집합에 추가

        for adjacent_node, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent_node]:
                distances[adjacent_node] = distance
                paths[adjacent_node] = paths[current_node] + [adjacent_node]
                heapq.heappush(queue, [distance, adjacent_node])

    sorted_paths = {node: paths[node] for node in sorted(paths)}

    return [distances, sorted_paths]

# TEST 코드
print(solution({ 'A': {'B': 9, 'C': 3}, 'B': {'A': 5}, 'C': {'B': 1} }, 'A'))
print(solution({'A': {'B': 1}, 'B': {'C': 5}, 'C': {'D': 1}, 'D': {}}, 'A'))
