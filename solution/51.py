from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
  maxdiff, max_comb = 0, {}

  # ➊ 주어진 조합에서 각각의 점수 계산
  def calculate_score(combi):
    score1, score2 = 0, 0
    for i in range(1, 11):
      if info[10 - i] < combi.count(i):
        score1 += i
      elif info[10 - i] > 0:
        score2 += i
    return score1, score2

  # ➋ 최대 차이와 조합 저장
  def calculate_diff(diff, cnt):
    nonlocal maxdiff, max_comb
    if diff > maxdiff:
      max_comb = cnt
      maxdiff = diff

  # ➌ 가능한 라이언의 과녁점수 조합의 모든 경우에 대해서 체크
  for combi in combinations_with_replacement(range(11), n):
    cnt = Counter(combi)
    score1, score2 = calculate_score(combi)
    diff = score1 - score2
    calculate_diff(diff, cnt)

  # ➍ 최대 차이가 0 이상인 경우, 조합 반환
  if maxdiff > 0:
    answer = [0] * 11
    for n in max_comb:
      answer[10 - n] = max_comb[n]
    return answer
  else:  # ➎ 최대 차이가 0인 경우, -1 반환
    return [-1]
