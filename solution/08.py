def solution(s):
  stack = [ ]
  for c in s:
    if c == "(":
      stack.append(c)
    elif c == ")":
      if not stack:
        return False
      else:
        stack.pop( ) 
  if stack:
    return False
  else:
    return True
