from itertools import permutations

def solution(n, weak, dist):
  # ➊ 주어진 weak 지점들을 선형으로 만들기 위해 weak 리스트에 마지막 지점 + n을 추가
  length = len(weak)
  for i in range(length):
    weak.append(weak[i] + n)

  # ➋ 투입할 수 있는 친구들의 수에 1을 더한 값을 초기값으로 설정
  answer = len(dist) + 1

  # ➌ 모든 weak 지점을 시작점으로 설정하며 경우의 수를 탐색
  for i in range(length):
    for friends in permutations(dist, len(dist)):
      # ➍ friends에 들어있는 친구들을 순서대로 배치하며 투입된 친구 수(cnt) 측정
      cnt = 1
      position = weak[i] + friends[cnt - 1]
      # ➎ 현재 투입된 친구가 다음 weak 지점까지 갈 수 있는지 검사
      for j in range(i, i + length):
        if position < weak[j]:
          cnt += 1
          # ➏ 투입 가능한 친구의 수를 초과한 경우 탐색 중단
          if cnt > len(dist):
            break
          position = weak[j] + friends[cnt - 1]
      # ➐ 최소 친구 수를 구함
      answer = min(answer, cnt)

  # ➑ 모든 경우의 수를 탐색한 결과가 투입 가능한 친구 수를 초과하는 경우, -1 반환
  return answer if answer <= len(dist) else -1
