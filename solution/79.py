def solution(strs, t):
  n = len(t)  # ➊ 타겟 문자열 t의 길이
  dp = [float("inf")] * (n + 1)  # ➋ 각 위치에서 필요한 최소 조각수를 저장할 배열(초기값은 INF로 함)
  dp[0] = 0  # ➌ 빈 문자열을 위해 필요한 최소 조각수는 0
  sizes = set(len(s) for s in strs)  # ➍ strs 조각들의 길이를 저장한 집합

  for i in range(1, n + 1):  # ➎ dp[i]부터 dp[n]까지 채우기 위한 반복문
    for size in sizes:  # ➏ 각 str 조각의 문자열 길이에 대하여
      if (
        i - size >= 0 and t[i - size : i] in strs
      ):  # ➐ 이미 구한 해와 strs 조각을 추가해서 문자열을 만들 수 있다면
        dp[i] = min(dp[i], dp[i - size] + 1)  # ➑ 해당 위치의 최소 조각수를 갱신
  return dp[n] if dp[n] < float("inf") else -1  # ➒ 최소 조각수를 반환
