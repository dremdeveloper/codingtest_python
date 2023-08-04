def solution(n):
  fib = [0, 1]  # F(0) = 0, F(1) = 1
  for i in range(2, n + 1):
    fib.append((fib[i - 1] + fib[i - 2]) % 1234567)
  return fib[n]
