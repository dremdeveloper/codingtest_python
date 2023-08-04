def solution(board, aloc, bloc):
  # ➊ 게임판의 행과 열의 개수를 저장합니다.
  ROW, COL = len(board), len(board[0])
  # ➋ 이동할 수 있는 방향을 저장합니다. 상, 우, 하, 좌 순서로 저장되어 있습니다.
  DR, DC = [-1, 0, 1, 0], [0, 1, 0, -1]

  # ➌ 주어진 위치가 유효한 위치인지 확인하는 함수입니다.
  def is_valid_pos(r, c):
    return 0 <= r < ROW and 0 <= c < COL

  # ➍ 재귀적으로 호출되는 함수입니다.
  def recursive_func(alpha_pos, beta_pos, visited, step):
    # ➎ 현재 플레이어의 위치와 이동 가능한지 여부,
    # 상대 플레이어가 이긴 경우를 저장하는 변수들입니다.
    r, c = alpha_pos if step % 2 == 0 else beta_pos
    can_move = False
    is_opponent_winner = True
    # ➏ 이긴 경우와 지는 경우를 저장하는 리스트입니다.
    win_steps, lose_steps = [], []

    # ➐ 현재 위치에서 이동할 수 있는 모든 방향으로 이동해봅니다.
    for i in range(4):
      nr, nc = r + DR[i], c + DC[i]
      # ➑ 이동할 수 있는 위치인 경우
      if is_valid_pos(nr, nc) and (nr, nc) not in visited and board[nr][nc]:
        can_move = True
        # ➒ 두 플레이어의 위치가 같으면 A 플레이어가 이긴 것이므로 True와 step + 1을 반환합니다.
        if alpha_pos == beta_pos:
          return True, step + 1

        # ➓ 재귀적으로 호출하여 이긴 여부와 남은 턴수를 가져옵니다.
        win, steps_left = (
          recursive_func([nr, nc], beta_pos, visited | {(r, c)}, step + 1)
          if step % 2 == 0
          else recursive_func(
            alpha_pos, [nr, nc], visited | {(r, c)}, step + 1
          )
        )
        # ⓫ 상대 플레이어가 이긴 경우만 True로 유지합니다.
        is_opponent_winner &= win
        # ⓬ 이긴 경우와 지는 경우를 저장합니다.
        (win_steps if win else lose_steps).append(steps_left)

    # ⓭ 이동할 수 있는 위치가 없는 경우
    if not can_move:
      return False, step
    # ⓮ 상대 플레이어가 이긴 경우
    if is_opponent_winner:
      return False, max(win_steps)
    # ⓯ 현재 플레이어가 이긴 경우
    return True, min(lose_steps)

  # ⓰ A 플레이어가 이길 때까지 걸리는 최소 턴 수를 반환합니다.
  _, steps = recursive_func(aloc, bloc, set(), 0)
  return steps
