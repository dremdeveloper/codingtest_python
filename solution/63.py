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
