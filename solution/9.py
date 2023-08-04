def solution(decimal):
  stack = [ ]
  while decimal > 0:
    remainder = decimal % 2
    stack.append(str(remainder))
    decimal //= 2
  binary = ""
  while stack:
    binary += stack.pop( ) 
  return binary
