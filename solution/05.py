def solution(arr1, arr2):
  # ➊ 행렬 arr1과 arr2의 행과 열의 수
  r1, c1 = len(arr1), len(arr1[0])
  r2, c2 = len(arr2), len(arr2[0])
  
  # ➋ 결과를 저장할 2차원 리스트 초기화
  ret = [[0] * c2 for _ in range(r1)]

  # ➌ 첫 번째 행렬 arr1의 각 행과 두 번째 행렬 arr2의 각 열에 대해
  for i in range(r1):
    for j in range(c2):
      # ➍ 두 행렬의 데이터를 곱해 결과 리스트에 더해줌
      for k in range(c1):
        ret[i][j] += arr1[i][k] * arr2[k][j]
  return ret
