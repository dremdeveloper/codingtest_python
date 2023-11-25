def solution(s):
  counts = [0] * 26  # ❶ 알파벳 개수(26개)만큼 빈도수 배열 생성

  # ❷ 문자열의 각 문자에 대한 빈도수를 빈도수 배열에 저장
  for c in s:
    counts[ord(c) - ord("a")] += 1

  # ❸ 빈도수 배열을 순회하면서 정렬된 문자열을 생성
  sorted_str = ""
  for i in range(26):
    sorted_str += chr(i + ord("a")) * counts[i]

  return sorted_str
  
  
# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution('hello')) # 반환값 : 'ehllo'
print(solution('algorithm')) # 반환값 : 'aghilmort'
