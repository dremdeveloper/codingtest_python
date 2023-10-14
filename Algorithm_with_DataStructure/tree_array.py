# 트리를 배열로 구현하는 예시:

# 트리는 일반적으로 노드와 간선으로 구성되며, 노드는 부모-자식 관계를 가집니다.
# 배열로 트리를 구현할 때, 인덱스를 활용해 부모 노드와 자식 노드 간의 관계를 표현합니다.
# 예를 들어, 인덱스 i의 노드의 왼쪽 자식 노드는 2*i, 오른쪽 자식 노드는 2*i + 1로 표현할 수 있습니다.
# 이 방법은 O(1)의 시간 복잡도를 가지며, 부모 노드와 자식 노드 간의 관계를 빠르게 파악할 수 있습니다.
# 그러나 모든 노드가 채워져 있지 않다면 메모리가 낭비될 수 있습니다.

# 도식화:
# 예를 들어, 다음과 같은 트리를 생각해 봅시다.
#     1
#    / \
#   2   3
#  / \ / \
# 4  5 6  7
# 이 트리를 배열로 표현하면 다음과 같습니다.
# [None, 1, 2, 3, 4, 5, 6, 7]
# (None은 트리의 루트가 1번 인덱스에 위치하도록 하기 위한 dummy 데이터입니다.)

# 트리를 배열로 표현
tree = [None, 1, 2, 3, 4, 5, 6, 7]

def get_left_child_idx(idx):
    return 2 * idx

def get_right_child_idx(idx):
    return 2 * idx + 1

# 루트 노드의 값 출력
print("Root node:", tree[1])

# 루트 노드의 왼쪽 자식 노드 값 출력
left_idx = get_left_child_idx(1)
print("Left child of root node:", tree[left_idx])

# 루트 노드의 오른쪽 자식 노드 값 출력
right_idx = get_right_child_idx(1)
print("Right child of root node:", tree[right_idx])

# 특정 노드 (예: 인덱스 3)의 왼쪽과 오른쪽 자식 노드 값 출력
node_idx = 3
print(f"Node at index {node_idx}:", tree[node_idx])
print(f"Left child of node at index {node_idx}:", tree[get_left_child_idx(node_idx)])
print(f"Right child of node at index {node_idx}:", tree[get_right_child_idx(node_idx)])
