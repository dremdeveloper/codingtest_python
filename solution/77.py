def solution(money):
  # ➊ 점화식에 필요한 변수를 초기화
  n = len(money)
  dp1 = [0] * n
  dp2 = [0] * n

  # ➋ 첫 번째 집을 도둑질하는 경우
  dp1[0] = money[0]
  dp1[1] = money[0]
  for i in range(2, n - 1):
    dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

  # ➌ 첫 번째 집을 도둑질하지 않는 경우
  dp2[1] = money[1]
  for i in range(2, n):
    dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

  # ➍ 두 경우 중 최댓값 찾기
  answer = max(dp1[-2], dp2[-1])
  return answer
