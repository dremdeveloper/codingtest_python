
def solution(want, number, discount):
  # ➊ want 리스트를 딕셔너리로 변환
  want_dict = { }
  for i in range(len(want)):
    want_dict[want[i]] = number[i]

  answer = 0  # ➋ 총 일수를 계산할 변수 초기화

  # ➌ 특정일 i에 회원가입 시 할인받을 수 있는 품목 체크
  for i in range(len(discount) - 9):
    discount_10d = { }  # ➍ i일 회원가입 시 할인받는 제품 및 개수를 담을 딕셔너리

    # ➎ i일 회원가입 시 할인받는 제품 및 개수로 딕셔너리 구성
    for j in range(i, i + 10):
      if discount[j] in want_dict:
        discount_10d[discount[j]] = discount_10d.get(discount[j], 0) + 1

    # ➏ 할인하는 상품의 개수가 원하는 수량과 일치하면 정답 변수에 1 추가
    if discount_10d == want_dict:
      answer += 1

  return answer
