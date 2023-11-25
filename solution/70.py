def solution(str1, str2):
 # ❶ 두 문자열의 길이를 저장 
  m = len(str1)
  n = len(str2)

  # ❷ LCS를 저장할 테이블 초기화
  dp = [[0] * (n + 1) for _ in range(m + 1)]

  # ❸ 동적 프로그래밍을 통해 LCS 길이 계산
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      # ❹ 현재 비교하는 문자가 같으면
      if str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      # ❺ 현재 비교하는 문자가 같지 않으면
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

  # ❻ LCS 길이 반환
  return dp[m][n]
  
# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution("ABCBDAB","BDCAB")) # 반환값 : 4
# print(solution("AGGTAB","GXTXAYB")) # 반환값 : 4
