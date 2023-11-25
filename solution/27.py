# ➊ 노드 클래스 정의
class Node:
  # ➋ 노드 클래스 생성자
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key

# ➌ 이진 탐색 트리 클래스
class BST:
  # ➍ 초기에 아무 노드도 없는 상태
  def __init__(self):
    self.root = None
  # ➎ 루트 노드부터 시작해서 이진 탐색 트리 규칙에 맞는 위치에 새 노드 삽입
  def insert(self, key):
    # 루트 노드가 없는 경우 새로운 노드를 루트 노드로 추가
    if not self.root:
      self.root = Node(key)
    else:
      curr = self.root
      while True:
        # 삽입하려는 값이 현재 노드의 값보다 작은 경우 왼쪽 자식 노드로 이동
        if key < curr.val:
          if curr.left:
            curr = curr.left
          else:
            # 현재 노드의 왼쪽 자식 노드가 없는 경우 새로운 노드 추가
            curr.left = Node(key)
            break
        else:
          # 삽입하려는 값이 현재 노드의 값보다 큰 경우 오른쪽 자식 노드로 이동
          if curr.right:
            curr = curr.right
          else:
            # 현재 노드의 오른쪽 자식 노드가 없는 경우 새로운 노드 추가
            curr.right = Node(key)
            break
  # ➏ 이진 탐색 규칙에 따라 특정값이 있는지 확인(루트 노드부터 시작)
  def search(self, key):
    curr = self.root
    # 현재 노드가 존재하고, 찾으려는 값과 현재 노드의 값이 같지 않은 경우 반복
    while curr and curr.val != key:
      # 찾으려는 값이 현재 노드의 값보다 작은 경우 왼쪽 자식 노드로 이동
      if key < curr.val:
        curr = curr.left
      else:
        # 찾으려는 값이 현재 노드의 값보다 큰 경우 오른쪽 자식 노드로 이동
        curr = curr.right
    return curr
# ➐ lst에 있는 데이터를 활용해서 이진 탐색 트리 생성, search_lst 원소 탐색
def solution(lst, search_lst):
  bst = BST()
  # 리스트의 각 요소를 이용하여 이진 탐색 트리 생성
  for key in lst:
    bst.insert(key)
  result = []
  # 검색 리스트의 각 요소를 이진 탐색 트리에서 검색하고, 검색 결과를 리스트에 추가
  for search_val in search_lst:
    if bst.search(search_val):
      result.append(True)
    else:
      result.append(False)
  return result
  
  
# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6])) # [True, True, True, False]
# print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])) # [False, False, False, False, False] 
