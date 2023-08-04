# ➊ 퀸이 서로 공격할 수 없는 위치에 놓이는 경우의 수를 구하는 함수
def getAns(n, y, width, diagonal1, diagonal2):
  ans = 0
  # ➋ 모든 행에 대해서 퀸의 위치가 결정되었을 경우
  if y == n:
    # ➌ 해결 가능한 경우의 수를 1 증가시킴
    ans += 1
  else:
    # ➍ 현재 행에서 퀸이 놓일 수 있는 모든 위치를 시도
    for i in range(n):
      # ➎ 해당 위치에 이미 퀸이 있는 경우, 대각선 상에 퀸이 있는 경우 스킵
      if width[i] or diagonal1[i + y] or diagonal2[i - y + n]:
        continue
      # ➏ 해당 위치에 퀸을 놓음
      width[i] = diagonal1[i + y] = diagonal2[i - y + n] = True
      # ➐ 다음 행으로 이동하여 재귀적으로 해결 가능한 경우의 수 찾기
      ans += getAns(n, y + 1, width, diagonal1, diagonal2)
      # ➑ 해당 위치에 놓인 퀸을 제거함
      width[i] = diagonal1[i + y] = diagonal2[i - y + n] = False
  return ans

def solution(n):
  # ➒ getAns 함수 호출하여 해결 가능한 경우의 수 찾기
  ans = getAns(n, 0, [False] * n, [False] * (n * 2), [False] * (n * 2))
  return ans
