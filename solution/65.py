def solution(s):
  # ❶ 이진 변환 횟수를 저장하는 변수
  count_transform = 0
  # ❷ 제거된 모든 0의 개수를 저장하는 변수
  count_zero = 0

  # ❸ s가 '1'이 아닌 동안 계속 반복
  while s != "1":
    # ❹ 이진 변환 횟수를 1 증가
    count_transform += 1
    # ❺ s에서 '0'의 개수를 세어 count_zero에 누적
    count_zero += s.count("0")
    # ❻ s에서 '1'의 개수를 세고, 이를 이진수로 변환
    # 최종 결과값에서 "0b" 제거
    s = bin(s.count("1"))[2:]

  # ➐ 이진 변환 횟수와 제거된 모든 '0'의 개수를 리스트에 담아 반환
  return [count_transform, count_zero]
