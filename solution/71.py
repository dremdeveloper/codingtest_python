# 답안 코드는 lis라고 되어있는데, 다른 문제와 통일하기 위해 lis로 구현했습니다. lis로 구현하신 경우 Test 코드에서도 lis로 이름을 바꿔주셔야 실행 됩니다.

def solution(nums):
  n = len(nums)

  # ❶ dp[i]는 nums[i]를 마지막으로 하는 LIS의 길이를 저장하는 배열입니다.
  dp = [1] * n

  for i in range(1, n):
    for j in range(i):
      # ❷ nums[i]와 nums[j]를 비교하여, nums[i]가 더 큰 경우에만 처리합니다.
      if nums[i] > nums[j]:
        # ❸ nums[i]를 이용하여 만든 부분 수열의 길이와
        # nums[j]를 이용하여 만든 부분 수열의 길이 + 1 중 최댓값을 저장합니다.
        dp[i] = max(dp[i], dp[j] + 1)

  # ❹ dp 배열에서 최댓값을 찾아 최장 증가 부분 수열의 길이를 반환합니다.
  return max(dp)
  
# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([1, 4, 2, 3, 1, 5, 7, 3])) # 반환값 : 5
# print(solution([3, 2, 1])) # 반환값 : 1
