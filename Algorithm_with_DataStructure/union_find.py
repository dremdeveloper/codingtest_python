#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. 알고리즘의 개념:
#    Union-Find는 Disjoint Set을 표현할 때 사용하는 알고리즘으로, 두 특성 - union과 find를 기반으로 합니다.
#    - Union: 두 개의 집합을 하나의 집합으로 합칩니다.
#    - Find: 주어진 원소가 어떤 집합에 포함되어 있는지 찾습니다.
#    랭크 기반과 경로 압축 기술을 사용하여 알고리즘의 시간 복잡도를 개선합니다.

# 2. 예시 입력 / 출력:
#    입력: unions = [(1, 2), (2, 3), (4, 5)]
#    출력: find(3) -> 1, find(4) -> 4

# 3. 알고리즘의 시간 복잡도:
#    - Union: O(α(n)) (α(n)은 아커만 함수의 역함수, 거의 상수 시간에 가깝습니다)
#    - Find: O(α(n))

# 4. 해당 알고리즘으로 풀 수 있는 문제 예시:
#    - 그래프에서 사이클 판별
#    - 네트워크 연결성 확인

# 5. 상세과정:
#    - 랭크 기반: 각 노드의 랭크(트리의 높이)를 유지하면서, 랭크가 높은 트리 아래에 랭크가 낮은 트리를 합칩니다.
#    - 경로 압축: Find 연산 시, 노드에서 루트 노드까지의 경로를 플래튼화하여 이후 연산의 속도를 높입니다.

# 각 노드의 부모 노드 정보
parent = [i for i in range(6)]  
# 각 노드의 랭크 (트리의 높이)
rank = [0] * 6  

def find(x):
    # 경로 압축 기법: 루트 노드를 찾으면서, 경로상의 노드들의 부모 노드를 루트 노드로 갱신
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    # 랭크 기반 합치기: 랭크가 더 높은 트리에 랭크가 낮은 트리를 합침
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1

# 예시 코드 실행
union(1, 2)
union(2, 3)
union(4, 5)

print(find(3))  # 출력: 1
print(find(4))  # 출력: 4

