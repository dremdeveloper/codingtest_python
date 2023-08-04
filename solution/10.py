def solution(s):
  answer = 0
  n = len(s)
  for i in range(n):
    stack = [ ]
    for j in range(n):
      # ➊ 괄호 문자열을 회전시키면서 참조
      c = s[(i + j) % n]
      if c == "(" or c == "[" or c == "{":  # ➋ 열린 괄호는 푸시
        stack.append(c)
      else:
        if not stack:  # ➌ 짝이 맞지 않는 경우
          break
      
         # ➍ 닫힌 괄호는 스택의 top과 짝이 맞는지 비교
        if c == ")" and stack[-1] == "(":
           stack.pop( ) 
        elif c == "]" and stack[-1] == "[":
           stack.pop( ) 
        elif c == "}" and stack[-1] == "{":
           stack.pop( ) 
        else:
             break
    else:  # ➎ for문이 break에 의해 끝나지 않고 끝까지 수행된 경우
      if not stack:
        answer += 1
  return answer
