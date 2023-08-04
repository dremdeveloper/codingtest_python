def solution(d, budget):
  d.sort()  # ➊ 배열 d를 오름차순으로 정렬
  count = 0  # ➋ 지원할 수 있는 부서의 개수를 세는 변수

  for amount in d:
    if budget < amount:
      break  # ➌ 남은 예산이 신청한 금액보다 작으면 더 이상 지원할 수 없으므로 종료
    budget -= amount  # ➍ 예산에서 신청한 금액을 차감
    count += 1

  return count if budget >= 0 else count - 1
