# ➊ polynomial hash를 구현한 부분
def polynomial_hash(str):
  p = 31  # 소수
  m = 1_000_000_007  # 버킷 크기
  hash_value = 0
  for char in str:
    hash_value = (hash_value * p + ord(char)) % m
  return hash_value
  
def solution(string_list, query_list):
  # ➋ string_list의 각 문자열에 대해 다항 해시값을 계산
  hash_list = [polynomial_hash(str) for str in string_list]

  # ➌ query_list의 각 문자열이 string_list에 있는지 확인
  result = [ ]
  for query in query_list:
    query_hash = polynomial_hash(query)
    if query_hash in hash_list:
      result.append(True)
    else:
      result.append(False)
  return result

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"] )) # 반환값 : [True, False, False, True]
