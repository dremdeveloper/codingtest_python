# 제대로 알고 구현하기
코딩테스트 문제를 분석하고 실제 알고리즘을 구현할 때, 여러가지 난관이 부딪힐 수 있습니다.  가장 많은 분들이 공부하다가 어려움을 느끼시는 경우는 크게 두 가지일 것입니다. </br></br>첫 번째는 문제를 이해하고 알맞은 알고리즘을 적용했는데도 시간초과가 발생하는 경우 입니다. 결국엔 해결하지 못하고 정답코드를 봤는데도 본인이 구현한 코드와 별 다를게 없어보입니다. 이 경우 대부분 원인은 알고리즘 구현을 위해 사용한 파이썬에서 제공한 함수들이, 생각보다 많은 연산을 하는 경우 입니다.  본인이 직접 구현하지 않고 이미 제공하는 함수 들을 그냥 바로 쓰기 때문에 제대로 공부하지 않으면 놓치기 쉬운 부분 입니다. 따라서 파이썬에서 제공하는 함수들의 시간복잡도를 제대로 파악하는 것이 중요 합니다. 
</br></br>두 번째는 문법적 오류가 발생한 경우 입니다.  한 번에 에러없이 구현하면 좋겠지만 대 부분의 경우 디버깅 과정을 거쳐서 구현을 하게 됩니다. 따라서 문법적 오류가 발생할 때 출력되는 에러메시지의 의미를 명확히 파악하는것이 중요합니다.
</br></br>본 장에서는, 먼저 코딩테스트에서 자주 사용되는 파이썬 함수들의 시간 복잡도를 알아본 다음 자주 발생하는 오류메시지 및 이를 조치하는 방법에 대해 설명하겠습니다. 


# 파이썬 함수의 시간 복잡도
## 리스트
배열 기반의 구조로, 인덱스를 활용한 접근 및 맨 끝부분에서 추가및 제거가 빠릅니다. 하지만 원소의 중간에서 삽입/삭제 하거나 왼소의 맨 처음에 삽입하는 경우에는 상당히 비효율적입니다. 아래 list는 임의 변수이름 입니다.  아래 표에서 lst는 리스트 타입의 변수 입니다.


| 메서드   | 동작                                    | 시간복잡도|
| ---------- | ---------------------------------------------- |------------------------------ |
| lst.append(item)    | item을 lst의 맨 끝에 추가                                    | O(1) |
| lst.insert(idx,item)    | item을 lst의 idx 위치에 삽입</br>(그 이후 원소들은 한칸씩 밀림) | O(N),N은 lst의 길이          |  
| lst.pop()    | lst의 마지막 원소 제거 후, 해당 원소 반환                                    | O(1) |
| lst.pop(0)    | lst의 첫 번째 원소 제거 후 해당 원소 반환</br>(모든 원소가 앞으로 한 칸씩 이동)| O(N),N은 lst의 길이 |
| lst.remove(item)    | lst에서 item과 일치하는 첫번째 원소 찾아서 제거                                    | O(N),N은 lst의 길이 |
| lst.extend(s)    | lst모든 원소들을 현재 리스트의 끝에 추가                                    | O(N),N은 lst의 길이 |
| lst[K]    | lst의 k번째 인덱스에 있는 요소를 반환합니다.                                    | O(1) |
| lst1 + lst2    | lst1와 lst2의 원소들을 하나의 리스트를 결합하고, 해당 리스트를 반환                                    | O(N+M), N은 lst1의 길이이고, M은 lst2의 길이 |
| list(set)   | set을 list로 변환 후 반환                                    | O(N), N은 set의 길이 |
| item in lst    | lst에 K가 있는지 확인 한후, True 혹은 False 반환                                    | O(N) N은 lst의 길이 |

## 덱
덱은 내부적으로 이중 연결 리스트로 구현되어 있습니다. 양쪽 끝에서 추가 및 제거 작업이 매우 빠릅니다. 삽입/삭제 연산 모두 시간복잡도 O(1) 입니다. 하지만 리스트와 마찬가지로 중간에서 삽입/삭제는 느립니다. 인덱스를 활용해서 접근할 수는 있지만, 인덱스 접근 연산은 덱의 원소개수가 N개일때, 시간복잡도가 O(N)이므로 리스트에 비해 느립니다.  아래 표에서 deq는 덱 타입의 변수 입니다.

| 메서드   | 동작                                    | 시간복잡도|
| ---------- | ---------------------------------------------- |------------------------------ |
| deq.append(item) | item을 deq의 오른쪽 끝에 추가 |O(1) |
| deq.appendleft(item) | item을 deq의 왼쪽 끝에 추가 |O(1) |
| deq.popleft() | deq의 오른쪽 끝에 있는 원소를 제거하고, 그 원소를 반환 |O(1) |
| deq[K] | deq의 K번째 위치에 있는 원소를 반환 |O(N), N은 deq의 길이 |


<작업중>
