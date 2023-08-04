def solution(lst):
  unique_lst = list(set(lst)) # ➊ 중복값 제거
  unique_lst.sort(reverse=True) # ➋ 내림차순 정렬 
  return unique_lst
