def solution(decimal):
    stack = []
    while decimal > 0:
        remainder = decimal % 2
        stack.append(str(remainder))
        decimal //= 2
    stack.reverse()
    return ''.join(stack)
    
    
# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution(10)) #반환값 :  1010
# print(solution(27)) #반환값 :  11011
# print(solution(12345)) #반환값 : 11000000111001
