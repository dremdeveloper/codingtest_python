from collections import Counter

def solution(topping):
  # ❶ 결과값을 저장할 변수 초기화
  split_count = 0

  # ❷ 토핑의 개수를 세어서 딕셔너리에 저장
  topping_counter = Counter(topping)

  # ❸ 절반에 속한 토핑의 종류를 저장할 집합
  half_topping_set = set()

  # ❹ 롤케이크를 하나씩 절반에 넣으면서 확인
  for t in topping:
    # ❺ 절반에 토핑을 추가하고, 해당 토핑의 전체 개수를 줄임
    half_topping_set.add(t)
    topping_counter[t] -= 1

    # ❻ 토핑의 전체 개수가 0이면 딕셔너리에서 제거
    if topping_counter[t] == 0:
      topping_counter.pop(t)

    # ❼ 토핑의 종류의 수가 같다면
    if len(half_topping_set) == len(topping_counter):
      split_count += 1

  # ❽ 공평하게 나눌 수 있는 방법의 수 반환
  return split_count
