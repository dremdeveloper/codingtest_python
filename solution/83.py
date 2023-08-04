def solution(people, limit):
  people.sort()  # ➊ 몸무게를 오름차순으로 정렬
  count = 0  # ➋ 필요한 보트 개수
  i = 0  # ➌ 가장 가벼운 사람을 가리키는 인덱스
  j = len(people) - 1  # ➍ 가장 무거운 사람을 가리키는 인덱스

  while i <= j:
    # ➎ 가장 무거운 사람과 가장 가벼운 사람을 같이 태울 수 있으면 두 사람 모두 보트에 태움
    if people[j] + people[i] <= limit:
      i += 1
    # ➏ 무거운 사람만 태울 수 있으면 무거운 사람만 보트에 태움
    j -= 1
    count += 1
  return count
