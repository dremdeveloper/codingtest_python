#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. 알고리즘의 개념:
#    LCS(Longest Common Subsequence) 알고리즘은 두 문자열에서 가장 긴 공통 부분 문자열을 찾는 알고리즘입니다.
#    동적 계획법(DP)를 사용하여 문제를 해결합니다.

# 2. 예시 입력 / 출력:
#    입력: "ABCBDAB", "BDCAB"
#    출력: "BCAB" (가장 긴 공통 부분 문자열)

# 3. 알고리즘의 시간 복잡도:
#    O(m*n), 여기서 m과 n은 각각 두 문자열의 길이입니다.

# 4. 해당 알고리즘으로 풀 수 있는 문제 예시:
#    - DNA 서열 정렬
#    - 텍스트 비교 및 유사도 측정

# 5. 상세과정:
#    - DP 테이블을 생성하여, 각 (i, j) 위치에 문자열1의 i번째까지의 문자와 문자열2의 j번째까지의 문자의 LCS 길이를 저장합니다.
#    - DP[i][j]의 값은 다음과 같이 계산됩니다:
#      - 문자열1의 i번째 문자와 문자열2의 j번째 문자가 같다면, DP[i][j] = DP[i-1][j-1] + 1
#      - 다르다면, DP[i][j] = max(DP[i-1][j], DP[i][j-1])

def LCS(X, Y):
    # DP 테이블 초기화
    dp = [[0] * (len(Y) + 1) for _ in range(len(X) + 1)]
    
    # DP 테이블 채우기
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[len(X)][len(Y)]

# 예시 코드 실행
X = "ABCBDAB"
Y = "BDCAB"
print(LCS(X, Y))  # 출력: 4

