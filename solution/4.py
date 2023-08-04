def solution(answers):
  # ➊ 수포자들의 패턴
  patterns = [
    [1, 2, 3, 4, 5], 
    [2, 1, 2, 3, 2, 4, 2, 5], 
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  ] 
  # ➋ 수포자들의 점수를 저장할 리스트
  scores = [0] * 3    
  # ➌ 각 수포자의 패턴과 정답이 얼마나 일치하는지 확인
  for i, answer in enumerate(answers):
    for j, pattern in enumerate(patterns):
      if answer == pattern[i % len(pattern)]:
        scores[j] += 1  
  # ➍ 가장 높은 점수 저장
  max_score = max(scores)
  # ➎ 가장 높은 점수를 가진 수포자들의 번호를 찾아서 리스트에 담음
  highest_scores = [ ]
  for i, score in enumerate(scores):
    if score == max_score:
      highest_scores.append(i + 1)
  return highest_scores
