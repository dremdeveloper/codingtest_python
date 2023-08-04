def solution(triangle):
  n = len(triangle)
  dp = [[0] * n for _ in range(n)]  # ➊ dp 테이블 초기화

  # ➋ dp 테이블의 맨 아래쪽 라인 초기화
  for i in range(n):
    dp[n - 1][i] = triangle[n - 1][i]

  # ➌ 아래쪽 라인부터 올라가면서 dp 테이블 채우기
  for i in range(n - 2, -1, -1):
    for j in range(i + 1):
      dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

  return dp[0][0]  # 꼭대기에서의 최댓값 반환
