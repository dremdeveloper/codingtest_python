def solution(nums):
  num_set = set(nums)  # ➊ nums 리스트에서 중복을 제거한 집합(set)을 구함
  n = len(nums)  # ➋ 폰켓몬의 총 수
  k = n // 2  # ➌ 선택할 폰켓몬의 수
  return min(k, len(num_set))  # ➍ 중복을 제거한 폰켓몬의 종류 수와 선택할 폰켓몬의 수 중 작은값 반환