def solution(arr, n):
  # ❶ 2차원 배열을 인자로 받고, 90도 회전시키는 함수
  def rotate_90(arr):
    # ❷ 배열의 크기를 저장
    n = len(arr)

    # ❸ 배열의 크기와 동일한 2차원 배열 생성(초기값은 0)
    rotated_arr = [[0] * n for _ in range(n)]

    # ❹ 배열을 90도회전
    for i in range(n):
      for j in range(n):
        rotated_arr[j][n - i - 1] = arr[i][j]

    # ❺ 90도로 회전한 배열 반환
    return rotated_arr

  # ❻ 원본배열 arr을 복사
  rotated_arr = arr.copy()

  # ❼ 90도 회전 함수 호출
  for _ in range(n):
    rotated_arr = rotate_90(rotated_arr)

  return rotated_arr

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
'''
print(solution(
[
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14, 15, 16]
], 1))
'''

'''
반환값 : 
[
[13, 9, 5, 1],
[14, 10, 6, 2],
[15, 11, 7, 3],
[16, 12, 8, 4]
]
'''
    
'''    
print(solution(
[
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14,15,16]
 ], 2))
'''

'''
반환값 : 
[
[16, 15, 14, 13],
[12, 11, 10, 9],
[8, 7, 6, 5],
[4, 3, 2, 1]
]
'''
