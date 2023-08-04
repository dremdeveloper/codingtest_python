def solution(n):
  digits = list(str(n))  # ➊ 정수 n을 문자열로 변환하고 각 자릿수를 리스트로 저장합니다.
  digits.sort(reverse=True)  # ➋ 내림차순으로 정렬합니다.
  answer = int("".join(digits))  # ➌ 정렬된 자릿수를 다시 하나의 문자열로 합쳐 정수로 변환합니다.
  return answer
