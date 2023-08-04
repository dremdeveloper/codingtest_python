def solution(numbers):
  ret = [ ]  # ➊ 빈 배열 생성
  # ➋ 두 수를 선택하는 모든 경우의 수를 반복문으로 구함
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      # ➌ 두 수를 더한 결과를 새로운 배열에 추가
      ret.append(numbers[i] + numbers[j])
  # ➍ 중복된 값을 제거하고, 오름차순으로 정렬
  ret = sorted(list(set(ret)))
  return ret  # ➎ 최종 결과 반환
