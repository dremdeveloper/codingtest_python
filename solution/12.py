def solution(prices):
  n = len(prices)
  answer = [0] * n  # ➊ 가격이 떨어지지 않은 기간을 저장할 배열

  # 스택(stack)을 사용해 이전 가격과 현재 가격을 비교
  stack = [0]  # ➋ 스택 초기화
  for i in range(1, n):
    while stack and prices[i] < prices[stack[-1]]:
      # ➌ 가격이 떨어졌으므로 이전 가격의 기간을 계산
      j = stack.pop( ) 
      answer[j] = i - j
    stack.append(i)
  # ➍ 스택에 남아 있는 가격들은 가격이 떨어지지 않은 경우
  while stack:
    j = stack.pop( ) 
    answer[j] = n - 1 - j
  return answer
