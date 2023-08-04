def solution(id_list, report, k):
  reported_user = { }  # 신고당한 유저 - 신고 유저 집합을 저장할 딕셔너리
  count = { }  # 처리 결과 메일을 받은 유저 - 받은 횟수를 저장할 딕셔너리
  # ➊ 신고 기록 순회
  for r in report:
    user_id, reported_id = r.split( ) 
    if reported_id not in reported_user:  # ➋ 신고당한 기록이 없다면
      reported_user[reported_id] = set( ) 
    reported_user[reported_id].add(user_id)  # ➌ 신고한 사람의 아이디를 집합에 담아 딕셔너리에 연결
  for reported_id, user_id_lst in reported_user.items( ) :
    if len(user_id_lst) >= k:  # ➍ 정지 기준에 만족하는지 확인
      for uid in user_id_lst:  # ➎ 딕셔너리를 순회하며 count 계산
        if uid not in count:
          count[uid] = 1
        else:
          count[uid] += 1
  answer = [ ]
  for i in range(len(id_list)):  # ➏ 각 아이디별 메일을 받은 횟수를 순서대로 정리
    if id_list[i] not in count:
      answer.append(0)
    else:
      answer.append(count[id_list[i]])
  return answer
