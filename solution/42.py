from collections import deque

def solution(maps):
  # ➊ 이동할 수 있는 방향을 나타내는 배열 move 선언
  move = [[-1, 0], [0, -1], [0, 1], [1, 0]]

  # ➋ 맵의 크기를 저장하는 변수 선언
  n = len(maps)
  m = len(maps[0])

  # ➌ 거리를 저장하는 배열 dist를 -1로 초기화
  dist = [[-1] * m for _ in range(n)]

  # ➍ bfs 함수를 선언
  def bfs(start):
    # ➎ deque를 선언, 시작 위치를 deque에 추가
    q = deque([start])
    dist[start[0]][start[1]] = 1

    # ➏ deque가 빌 때까지 반복
    while q:
      here = q.popleft()

      # ➐ 현재 위치에서 이동할 수 있는 모든 방향
      for direct in move:
        row, column = here[0] + direct[0], here[1] + direct[1]

        # ➑ 이동한 위치가 범위를 벗어난 경우 다음 방향으로 넘어감
        if row < 0 or row >= n or column < 0 or column >= m:
          continue

        # ➒ 이동한 위치에 벽이 있는 경우 다음 방향으로 넘어
        if maps[row][column] == 0:
          continue

        # ➓ 이동한 위치가 처음 방문하는 경우, deque에 추가하고 거리 갱신
        if dist[row][column] == -1:
          q.append([row, column])
          dist[row][column] = dist[here[0]][here[1]] + 1

    # 거리를 저장하는 배열 dist를 반환
    return dist

  # 시작 위치에서 bfs( ) 함수를 호출하여 거리 계산
  bfs([0, 0])

  # 목적지까지의 거리 반환, 목적지에 도달하지 못한 경우 -1을 반환
  return dist[n - 1][m - 1]
