def solution(arr1, arr2):
  merged = []  # 정렬된 배열을 저장할 리스트 생성
  i, j = 0, 0  # 두 배열의 인덱스 초기화

  # 두 배열을 순회하면서 정렬된 배열을 생성
  while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
      merged.append(arr1[i])
      i += 1
    else:
      merged.append(arr2[j])
      j += 1

  # arr1이나 arr2 중 남아있는 원소들을 정렬된 배열 뒤에 추가
  while i < len(arr1):
    merged.append(arr1[i])
    i += 1
  while j < len(arr2):
    merged.append(arr2[j])
    j += 1

  return merged

  
# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([1, 3, 5], [2, 4, 6])) # 반환값 : [1, 2, 3, 4, 5, 6]
# print(solution([1, 2, 3], [4, 5, 6])) # 반환값 : [1, 2, 3, 4, 5, 6]
