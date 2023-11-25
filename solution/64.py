def solution(n):
  # ❶ n 크기의 2차원 배열 생성
  snail_array = [[0] * n for _ in range(n)]

  num = 1  # ❷ 달팽이 수열의 시작 숫자

  # ❸ 행과 열의 시작과 끝 인덱스를 설정
  start_row, end_row = 0, n - 1
  start_col, end_col = 0, n - 1

  while start_row <= end_row and start_col <= end_col:
    # ❹ 첫 번째 행 채우기
    for i in range(start_col, end_col + 1):
      snail_array[start_row][i] = num
      num += 1
    start_row += 1

    # ❺ 마지막 열 채우기
    for i in range(start_row, end_row + 1):
      snail_array[i][end_col] = num
      num += 1
    end_col -= 1

    # ❻ 마지막 행 채우기
    if start_row <= end_row:
      for i in range(end_col, start_col - 1, -1):
        snail_array[end_row][i] = num
        num += 1
      end_row -= 1

    # ❼ 첫 번째 열 채우기
    if start_col <= end_col:
      for i in range(end_row, start_row - 1, -1):
        snail_array[i][start_col] = num
        num += 1
      start_col += 1

  return snail_array


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution(3))

'''
반환값 : 
[
 [1, 2, 3],
 [8, 9, 4],
 [7, 6, 5]
]
'''

# print(solution(4))

'''
반환값 : 
[
 [1, 2, 3, 4],
 [12, 13, 14, 5],
 [11, 16, 15, 6],
 [10, 9, 8, 7]
]
'''
