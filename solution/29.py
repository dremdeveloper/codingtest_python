def solution(enroll, referral, seller, amount):
  # ➊ parent 딕셔너리 key는 enroll의 노드, value는 referral의 노드로 구성됨
  parent = dict(zip(enroll, referral))

  # ➋ total 딕셔너리 생성 및 초기화
  total = {name: 0 for name in enroll}

  # ➌ seller 리스트와 amount 리스트를 이용하여 이익 분배
  for i in range(len(seller)):
    # ➍ 판매자가 판매한 총 금액 계산
    money = amount[i] * 100
    cur_name = seller[i]
    # ➎ 판매자부터 차례대로 상위 노드로 이동하며 이익 분배
    while money > 0 and cur_name != "-":
      # ➏ 현재 판매자가 받을 금액 계산(10%를 제외한 금액)
      total[cur_name] += money - money // 10
      cur_name = parent[cur_name]
      # ➐ 10%를 제외한 금액 계산
      money //= 10

  # ➑ enroll 리스트의 모든 노드에 대해 해당하는 이익을 리스트로 반환
  return [total[name] for name in enroll]
