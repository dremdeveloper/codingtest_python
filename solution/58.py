def solution(array, commands):
  answer = []
  for cmd in commands:
    i, j, k = cmd
    sliced_arr = array[i - 1 : j]  # ➊ i번째부터 j번째까지 자르기
    sorted_arr = sorted(sliced_arr)  # ➋ 자른 배열을 정렬하기
    answer.append(sorted_arr[k - 1])  # ➌ k번째 원소 구하기
  return answer
