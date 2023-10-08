#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 조합(combinations)은 주어진 리스트 내에서 특정 개수 r의 원소를 선택하는 모든 가능한 조합을 생성합니다.
# 예를 들어, [1, 2, 3]에서 2개의 원소를 선택하는 경우: [(1, 2), (1, 3), (2, 3)]
# 시간 복잡도: O(nCr) = n! / (r! * (n-r)!) (모든 조합을 생성하므로)
# 이 코드는 재귀적으로 조합을 생성하고 그 결과를 리스트에 저장합니다.

# lst=[1,2,3]인 경우, 아래 주석과 맞춰서 보면 됩니다.
# 현재 원소를 선택하는 경우
        # e.g., lst = [1, 2, 3], r = 2
        # |-> 1을 선택: 
        # |       |
        # |       |-> 2를 선택: (1, 2) 완성

# 현재 원소를 선택하지 않는 경우
        # e.g., lst = [1, 2, 3], r = 2
        # |       |
        # |       |-> 2를 선택 X:
        # |               |
        # |               |-> 3를 선택: (1, 3) 완성

#초기 호출
        # e.g., lst = [1, 2, 3], r = 2
        # |-> 1을 선택 X:
        #         |
        #         |-> 2를 선택: 
        #         |       |
        #         |       |-> 3를 선택: (2, 3) 완성


def combinations(lst, r):
    result = []  # 최종 조합 결과를 담을 리스트
    
    def generate_combination(chosen, remain, n):
        """
        chosen: 지금까지 선택한 원소 리스트
        remain: 남은 원소 리스트
        n: 더 필요한 원소의 수
        """
        
        # 원하는 r개의 원소를 모두 선택한 경우, 결과에 추가
        if n == 0:
            result.append(chosen[:])  # 선택한 원소 리스트를 결과에 추가 (복사하여 추가)
            return

        # 남은 원소가 없거나, 더 이상 원소를 선택할 수 없는 경우 종료
        if not remain or len(remain) < n:
            return
        
        # 현재 원소를 선택하는 경우
        chosen.append(remain[0])  # 현재 원소를 chosen에 추가
        generate_combination(chosen, remain[1:], n-1)  # 다음 원소를 선택하기 위해 재귀 호출
        chosen.pop()  # 현재 원소를 다시 chosen에서 제거하여 다음 시뮬레이션을 위해 돌아감
        
        # 현재 원소를 선택하지 않는 경우
        generate_combination(chosen, remain[1:], n)  # 다음 원소를 선택하기 위해 재귀 호출
    
    # 초기 호출
    generate_combination([], lst, r) 
    
    return result

lst = [1, 2, 3]
r = 2
print(combinations(lst, r))
