#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. 자료구조 개념:
#    스택은 데이터의 삽입과 삭제가 한 쪽 끝에서만 일어나는 선형 자료구조이다. 
#    이러한 특성 때문에 Last In First Out (LIFO) 자료구조라고도 불린다. 
#    여기서는 deque라는 Python 라이브러리를 사용하여 스택을 구현하였다.

# 2. 예시 입력 / 출력:
#    입력: [1, 2, 3, 4, 5] (순차적으로 스택에 push)
#    출력: 5 4 3 2 1 (순차적으로 스택에서 pop)

# 3. 자료구조의 시간 복잡도:
#    스택의 주요 연산인 push와 pop 모두 O(1)의 시간 복잡도를 가진다. 
#    이는 각 연산이 상수 시간에 수행됨을 의미한다.

# 4. 해당 자료구조로 풀 수 있는 문제 예시:
#    - 괄호 짝 맞추기 문제
#    - 브라우저의 뒤로 가기 기능 구현
#    - 깊이 우선 탐색 (DFS) 등

# 5. 상세 과정:
#    - 먼저 deque 라이브러리를 사용하여 스택 객체를 초기화한다.
#    - append() 메서드를 사용하여 요소를 스택에 삽입한다.
#    - pop() 메서드를 사용하여 스택의 맨 위 요소를 제거하고 반환한다.
from collections import deque


# 스택 객체 초기화
stack = deque()

# 요소들을 스택에 삽입 (push)
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

# 스택에서 요소들을 제거 (pop)하면서 출력
while stack:
    print(stack.pop())  # 출력: 5, 4, 3, 2, 1 (LIFO 순서)
