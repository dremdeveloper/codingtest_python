def solution(land):
  # ➊ 각 행마다 이전 행에서의 최대 점수를 더해가며 최대 점수를 구합니다.
  for i in range(1, len(land)):
    for j in range(4):
      # ➋ 이전 행에서 현재 열의 값을 제외한 나머지 열들 중에서 가장 큰 값을 더해줍니다.
      land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1 :])

  # ➌ 마지막 행에서 얻을 수 있는 최대 점수를 반환합니다.
  return max(land[-1])
