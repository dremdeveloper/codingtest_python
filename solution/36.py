def solution(phone_book):
  # ➊ 전화번호부 정렬
  phone_book.sort( ) 

  # ➋ 전화번호부에서 연속된 두 개의 전화번호 비교
  for i in range(len(phone_book) - 1):
    if phone_book[i + 1].startswith(phone_book[i]):
      return False

  # ➌ 모든 전화번호를 비교한 후에도 반환되지 않았다면, 접두어가 없는 경우이므로 True 반환
  return True
