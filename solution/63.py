def multiply_matrices(matrix1, matrix2):
  # ❶ 결과 행렬을 0으로 초기화합니다.
  result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  # ❷ 행렬 곱셈을 수행합니다.
  for i in range(3):
    for j in range(3):
      for k in range(3):
        result[i][j] += matrix1[i][k] * matrix2[k][j]

  return result

def transpose_matrix(matrix):
  # ❸ 결과 행렬을 0으로 초기화합니다.
  result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  # 전치 행렬을 계산합니다.
  for i in range(3):
    for j in range(3):
      result[j][i] = matrix[i][j]

  return result

def solution(matrix1, matrix2):
  # 주어진 두 행렬을 곱합니다.
  multiplied = multiply_matrices(matrix1, matrix2)

  # 곱셈 결과의 전치 행렬을 계산합니다.
  transposed = transpose_matrix(multiplied)
  return transposed

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
'''
print(solution(
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
],

[
 [9, 8, 7],
 [6, 5, 4],
 [3, 2, 1]
]))
'''

'''
반환값 : 
[
 [30, 84, 138],
 [24, 69, 114],
 [18, 54, 90]
]
'''

'''    
print(solution(
[
 [2, 4, 6],
 [1, 3, 5],
 [7, 8, 9]
],

[
 [9, 1, 2],
 [4, 5, 6],
 [7, 3, 8]
]))
'''

'''
반환값 : 
[
 [76, 56, 158],
 [40, 31, 74],
 [76, 60, 134]
]
'''
