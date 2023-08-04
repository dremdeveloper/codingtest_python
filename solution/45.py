def solution(board):
  # ➊ 주어진 좌표가 보드의 범위 내에 있는지 확인
  def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

  # ➋ 주어진 좌표가 차단되었거나 이동할 수 없는지 확인
  def is_blocked(x, y):
    return (x, y) == (0, 0) or not is_valid(x, y) or board[x][y] == 1

  # ➌ 이전 방향과 현재 방향에 따라 비용을 계산
  def calculate_cost(direction, prev_direction, cost):
    if prev_direction == -1 or (prev_direction - direction) % 2 == 0:
      return cost + 100
    else:
      return cost + 600

  # ➍ 주어진 좌표와 방향이 아직 방문하지 않았거나 새 비용이 더 작은 경우
  def isShouldUpdate(x, y, direction, new_cost):
    return visited[x][y][direction] == 0 or visited[x][y][direction] > new_cost

  queue = [(0, 0, -1, 0)]
  N = len(board)
  directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
  visited = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
  answer = float("inf")

  # ➎ 큐가 빌 때까지 반복
  while queue:
    x, y, prev_direction, cost = queue.pop(0)

    # ➏ 가능한 모든 방향에 대해 반복
    for direction, (dx, dy) in enumerate(directions):
      new_x, new_y = x + dx, y + dy

      # ➐ 이동할 수 없는 좌표는 건너뛰기
      if is_blocked(new_x, new_y):
        continue

      new_cost = calculate_cost(direction, prev_direction, cost)

      # ➑ 도착지에 도달한 경우 최소 비용 업데이트
      if (new_x, new_y) == (N - 1, N - 1):
        answer = min(answer, new_cost)
      # ➒ 좌표와 방향이 아직 방문하지 않았거나 새 비용이 더 작은 경우 큐에 추가
      elif isShouldUpdate(new_x, new_y, direction, new_cost):
        queue.append((new_x, new_y, direction, new_cost))
        visited[new_x][new_y][direction] = new_cost

  return answer
