def solution(keyinput, board):
  # ❶ 캐릭터의 초기 위치
  x, y = 0, 0
  # ❷ 각 방향에 대한 움직임
  moves = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}
  # ❸ 게임 경계좌표
  width, height = board[0] // 2, board[1] // 2

  # ❹ 보드의 경계좌표를 벗어나는지 확인하는 함수
  def is_in_bounds(x, y, dx, dy):
    return -width <= x + dx <= width and -height <= y + dy <= height

  for key in keyinput:
    # ❺ 방향키에 따른 오프셋
    dx, dy = moves[key]
    # ❻ 게임 맵의 크기를 벗어나지 않는지 확인
    if is_in_bounds(x, y, dx, dy):
      x += dx
      y += dy

  # ❼ 캐릭터의 위치를 반환합니다.
  return [x, y]
