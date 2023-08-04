def lis(nums):
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
