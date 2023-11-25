def find(parents, x):
  # 루트 노드 찾는 함수
  if parents[x] == x:  # 만약 x의 부모가 자기 자신이면, 즉 x가 루트 노드라면
    return x
  # 그렇지 않다면 x의 부모를 찾아서 parents[x]에 저장하고,
  # 그 부모 노드의 루트 노드를 찾아서 parents[x]에 저장합니다.
  parents[x] = find(parents, parents[x])
  return parents[x]  # parents[x]를 반환합니다.


def union(parents, x, y):
  # 두 개의 집합을 합치는 함수
  root1 = find(parents, x)  # x가 속한 집합의 루트 노드 찾기
  root2 = find(parents, y)  # y가 속한 집합의 루트 노드 찾기

  parents[root2] = root1  # y가 속한 집합을 x가 속한 집합에 합침

def solution(k, operations):
  parents = list(range(k))  # 처음에는 각 노드가 자기 자신을 부모로 가지도록 초기화
  n = k  # 집합의 개수를 저장할 변수, 처음에는 모든 노드가 서로 다른 집합에 있으므로 k

  for op in operations:  # operations 리스트에 있는 연산들을 하나씩 처리
    if op[0] == "u":  # 'u' 연산이면
      union(parents, op[1], op[2])  # op[1]과 op[2]가 속한 집합을 합칩니다.
    elif op[0] == "f":  # 'f' 연산이면
      find(parents, op[1])  # op[1]이 속한 집합의 루트 노드를 찾습니다.

  # 모든 노드의 루트 노드를 찾아서 집합의 개수를 계산
  n = len(set(find(parents, i) for i in range(k)))

  return n  # 집합의 개수를 반환
  
   
# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution(3,[['u', 0, 1], ['u', 1, 2], ['f', 2]])) # 반환값 : 1
# print(solution(4,[['u', 0, 1], ['u', 2, 3], ['f', 0]])) # 반환값 : 2
