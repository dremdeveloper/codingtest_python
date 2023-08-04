from collections import Counter

def solution(k, tangerine):
  # ➊ 귤의 개수를 세는 Counter 객체 생성
  counter = Counter(tangerine)

  # ➋ 개수를 내림차순으로 정렬
  sorted_counts = sorted(counter.values(), reverse=True)

  num_types = 0  # ➌ 현재까지의 종류 수
  count_sum = 0  # ➍ 현재까지의 귤 개수 합

  for count in sorted_counts:
    count_sum += count
    num_types += 1

    # ➎ 귤 개수 합이 k 이상이 되는 순간 종료
    if count_sum >= k:
      break

  return num_types
