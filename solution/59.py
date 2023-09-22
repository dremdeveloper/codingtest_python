import functools

def compare(a, b):
  # ➊ 각 수를 문자열로 바꾼 뒤, 조합하여 비교하여 더 큰 수를 반환합니다.
  # 예. a=3, b=30 -> t1='330', t2='303' -> int(t1) > int(t2) -> 1 반환
  t1 = str(a) + str(b)
  t2 = str(b) + str(a)
  # t1이 크다면 1, t2가 크다면 -1, 같으면 0
  return (int(t1) > int(t2)) - (int(t1) < int(t2))

def solution(numbers):
  # ➋ reverse = True를 이용해 내림차순으로 정렬합니다.
  sorted_nums = sorted(
    numbers, key=functools.cmp_to_key(compare), reverse=True
  )
  # ➌ 각 정렬된 수를 문자열로 이어붙인 뒤, int로 변환한 값을 문자열로 다시 변환하여 반환합니다.
  answer = "".join(str(x) for x in sorted_nums)
  return "0" if int(answer) == 0 else answer
