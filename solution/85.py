def solution(N, stations, W):
  answer = 0
  location = 1  # ➊ 현재 탐색하는 아파트의 위치
  idx = 0  # ➋ 설치된 기지국의 인덱스


  while location <= N:
    # ➌ 기지국이 설치된 위치에 도달한 경우
    if idx < len(stations) and location >= stations[idx] - W:
      location = stations[idx] + W + 1
      idx += 1
    # ➍ 기지국이 설치되지 않은 위치인 경우
    else:
      location += 2 * W + 1  # ➎ 기지국을 설치하고 해당 범위를 넘어감
      answer += 1
  return answer
