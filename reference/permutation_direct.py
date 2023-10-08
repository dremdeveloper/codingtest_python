#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 순열(permutations)은 리스트 내 원소들을 모든 가능한 순서대로 배열하는 것을 의미합니다.
# 예를 들어, [1, 2, 3]의 순열은 [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]와 같이 2개씩 묶어서 모든 순서 조합을 생성합니다.
# 시간 복잡도: O(nPn) = n! (모든 순열을 생성하므로)
# 이 코드는 재귀적으로 순열을 생성하고 그 결과를 리스트에 저장합니다.

# 현재 원소를 선택하여 순열 생성, lst=[1,2,3]인 경우 
            # e.g., lst = [1, 2, 3], r = 2
            # |-> 1을 선택: 
            # |       |
            # |       |-> 2를 선택: (1, 2) 생성
            # |       |
            # |       |-> 3를 선택: (1, 3) 생성
            # |
            # |-> 2을 선택:
            # |       |
            # |       |-> 1를 선택: (2, 1) 생성
            # |       |
            # |       |-> 3를 선택: (2, 3) 생성
            # |
            # |-> 3을 선택:
            #         |
            #         |-> 1를 선택: (3, 1) 생성
            #         |
            #         |-> 2를 선택: (3, 2) 생성

def permutations(lst, r):
    result = []  # 최종 순열 결과를 담을 리스트

    def generate_permutation(chosen, remain):
        """
        chosen: 지금까지 선택한 원소 리스트
        remain: 남은 원소 리스트
        """
        # 원하는 r개의 원소를 모두 선택한 경우, 결과에 추가
        if len(chosen) == r:
            result.append(chosen[:])  # 선택한 원소 리스트를 결과에 추가 (복사하여 추가)
            return

        for i in range(len(remain)):
            # 현재 원소를 선택한 경우를 시뮬레이션하며 재귀 호출
            chosen.append(remain[i])  # 현재 원소를 chosen에 추가
            remaining_elements = remain[:i] + remain[i + 1:]  # remain에서 현재 원소를 제외
            generate_permutation(chosen, remaining_elements)
            chosen.pop()  # 현재 원소를 다시 chosen에서 제거하여 다음 시뮬레이션을 위해 돌아감

    generate_permutation([], lst)  # 초기 호출

    return result

lst = [1, 2, 3]
r = 2
print(permutations(lst, r))

