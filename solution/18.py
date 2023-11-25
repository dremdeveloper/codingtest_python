def count_sort(arr, k):
  # ➊ 해시 테이블 생성 및 초기화
  hashtable = [0] * (k + 1)

  for num in arr:
    # ➋ 현재 원소의 값이 k 이하인 때에만 처리
    if num <= k:
      # ➌ 현재 원소의 값을 인덱스로 해 해당 인덱스의 해시 테이블 값을 1로 설정
      hashtable[num] = 1
  return hashtable

def solution(arr, target):
  hashtable = count_sort(arr, target)

  for num in arr:
    complement = target - num
    # ➍ target에서 현재 원소를 뺀 값이 해시 테이블에 있는지 확인
    if (
      complement != num
      and complement >= 0
      and complement <= target
      and hashtable[complement] == 1
    ):
      return True
  return False
  
# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([1, 2, 3, 4, 8], 6)) # 반환값 : True
# print(solution([2, 3, 5, 9], 10)) # 반환값 : False
