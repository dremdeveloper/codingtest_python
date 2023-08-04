import math

def solution(progresses, speeds):
  answer = [ ]
  n = len(progresses)
  # ➊ 각 작업의 배포 가능일 계산
  days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]

  count = 0  # ➋ 배포될 작업의 수 카운트
  max_day = days_left[0]  # ➌ 현재 배포될 작업 중 가장 늦게 배포될 작업의 가능일

  for i in range(n):
    if days_left[i] <= max_day:  # ➍ 배포 가능일이 가장 늦은 배포일보다 빠르면
      count += 1
    else:  # ➎ 배포 예정일이 기준 배포일보다 느리면
      answer.append(count)
      count = 1
      max_day = days_left[i]

  answer.append(count)  # ➏ 마지막으로 카운트된 작업들을 함께 배포
  return answer
