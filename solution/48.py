def solution(board):
  def is_valid(num, row, col):
    # ❶ 현재 위치에 num이 들어갈 수 있는지 검사
    return not (in_row(num, row) or in_col(num, col) or in_box(num, row, col))

  def in_row(num, row):
    # ❷ 해당 행에 num이 있는지 확인
    return num in board[row]

  def in_col(num, col):
    # ❸ 해당 열에 num이 있는지 확인하는 함수
    return num in (board[i][col] for i in range(9))

  def in_box(num, row, col):
    # ❹ 현재 위치의 3x3 박스에 num이 있는지 확인
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
      for j in range(box_col, box_col + 3):
        if board[i][j] == num:
          return True
    return False

  def find_empty_position():
    # ❺ 스도쿠 보드에서 비어 있는 위치 반환
    for i in range(9):
      for j in range(9):
        if board[i][j] == 0:
          return i, j
    return None

  def find_solution():
    # ❻ 비어 있는 위치에 가능한 숫자를 넣어가며 스도쿠 해결
    empty_pos = find_empty_position()
    # ❼ 빈 칸이 없으면 스도쿠가 해결된 것으로 간주
    if not empty_pos:
      return True
    row, col = empty_pos
    for num in range(1, 10):
      if is_valid(num, row, col):
        board[row][col] = num
        if find_solution():  # ❽ 다음 빈 칸으로 재귀적으로 탐색
          return True
        board[row][col] = 0  # ❾ 가능한 숫자가 없으면 원래의 0으로 되돌림
    return False

  find_solution()
  return board


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
'''
print(solution(
[
 [5, 3, 0, 0, 7, 0, 0, 0, 0],
 [6, 0, 0, 1, 9, 5, 0, 0, 0],
 [0, 9, 8, 0, 0, 0, 0, 6, 0],
 [8, 0, 0, 0, 6, 0, 0, 0, 3],
 [4, 0, 0, 8, 0, 3, 0, 0, 1],
 [7, 0, 0, 0, 2, 0, 0, 0, 6],
 [0, 6, 0, 0, 0, 0, 2, 8, 0],
 [0, 0, 0, 4, 1, 9, 0, 0, 5],
 [0, 0, 0, 0, 8, 0, 0, 7, 9],
])
)
'''

'''
반환값 : 
[
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 9],
]
'''


'''
print(solution(
[
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
])
)
'''


'''
반환값 : 
[
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[4, 5, 6, 7, 8, 9, 1, 2, 3],
[7, 8, 9, 1, 2, 3, 4, 5, 6],
[2, 3, 4, 5, 6, 7, 8, 9, 1],
[5, 6, 7, 8, 9, 1, 2, 3, 4],
[8, 9, 1, 2, 3, 4, 5, 6, 7],
[3, 4, 5, 6, 7, 8, 9, 1, 2],
[6, 7, 8, 9, 1, 2, 3, 4, 5],
[9, 1, 2, 3, 4, 5, 6, 7, 8],
]
'''





