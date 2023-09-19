# 자료구조 및 알고리즘

이 저장소는 다양한 알고리즘과 데이터 구조에 관한 파이썬 코드를 담고 있습니다. 아래 표에서 각 파일에 대한 간단한 설명을 확인할 수 있습니다.

| 파일명 | 개념 | 시간 복잡도 | 적용 예 |
|--------|------|-------------|----------|
| [LCS_DP.py](Algorithm_with_DataStructure/LCS_DP.py) | LCS(Longest Common Subsequence) 알고리즘은 두 문자열에서 가장 긴 공통 부분 문자열을 찾는 알고리즘입니다. 동적 계획법(DP)를 사용하여 문제를 해결합니다. | O(m*n) (m과 n은 각각 두 문자열의 길이) | DNA 서열 정렬, 텍스트 비교 및 유사도 측정 |
| [LIS_DP.py](Algorithm_with_DataStructure/LIS_DP.py) | LIS(Longest Increasing Subsequence) 알고리즘은 주어진 배열에서 가장 긴 증가하는 부분 수열의 길이를 찾는 알고리즘이다. 동적 프로그래밍 방법을 사용하여 이전에 계산한 부분 문제의 결과를 저장하고 재사용함으로써 효율적으로 문제를 해결한다. | O(n²) | 주어진 배열에서 최장 증가 부분 수열의 길이를 찾는 문제, 시퀀스 정렬 문제에서 최적 부분 구조 찾기 등 |
| [bellmanford.py](Algorithm_with_DataStructure/bellmanford.py) | 벨만-포드 알고리즘은 그래프에서 주어진 시작 노드로부터 다른 모든 노드까지의 최단 경로를 찾는 알고리즘이다. 음수 가중치를 가진 간선도 처리할 수 있으나, 음수 사이클이 있는 경우에는 알고리즘이 작동하지 않는다. | O(V*E) (V: 노드의 수, E: 간선의 수) | 그래프에서 단일 출발점 최단 경로 문제, 음수 가중치가 있는 그래프에서의 최단 경로 문제 (단, 음수 사이클이 없어야 함) |
| [bfs.py](Algorithm_with_DataStructure/bfs.py) | BFS(너비 우선 탐색)는 그래프나 트리를 탐색하는 알고리즘 중 하나로, 루트 노드(혹은 다른 임의의 노드)에서 시작하여 인접한 노드들을 먼저 탐색하는 알고리즘입니다. 큐(Queue)를 사용하여 구현할 수 있으며, 아래 코드는 큐를 사용한 방법으로 BFS를 구현한 예입니다. | O(V + E) (V: 정점의 개수, E: 간선의 개수) | 최단 경로 찾기, 그래프의 연결성분 찾기 |
| [binary_search.py](Algorithm_with_DataStructure/binary_search.py) | 이진 탐색 알고리즘은 정렬된 리스트에서 특정 원소를 빠르게 찾기 위한 알고리즘입니다. 이 알고리즘은 리스트의 중간값을 기준으로 찾고자 하는 값이 중간값보다 큰지 작은지를 판단하며, 이를 반복하여 원하는 값을 찾습니다. | O(log n) | 정렬된 리스트에서 특정 원소 찾기 |
| [combination_generation.py](Algorithm_with_DataStructure/combination_generation.py) | 조합 생성 알고리즘은 주어진 리스트에서 n개의 원소를 선택하는 모든 가능한 조합을 생성하는 알고리즘입니다. |작성 예정 | 데이터 분석, 통계학에서 조합의 경우의 수를 구할 때 사용 |
| [dfs_recursion.py](Algorithm_with_DataStructure/dfs_recursion.py) | 깊이 우선 탐색(DFS)는 그래프나 트리를 탐색하는 알고리즘 중 하나로, 시작 노드에서 시작하여 더 이상 방문할 노드가 없을 때까지 깊게 탐색하는 알고리즘입니다. 이 코드는 재귀를 사용하여 구현되었습니다. |작성 예정 | 그래프 탐색, 경로 찾기 |
| [dfs_stack.py](Algorithm_with_DataStructure/dfs_stack.py) | 깊이 우선 탐색(DFS)는 그래프나 트리를 탐색하는 알고리즘 중 하나로, 시작 노드에서 시작하여 더 이상 방문할 노드가 없을 때까지 깊게 탐색하는 알고리즘입니다. 이 코드는 스택을 사용하여 구현되었습니다. |작성 예정 | 그래프 탐색, 경로 찾기 |
| [dijkstra.py](Algorithm_with_DataStructure/dijkstra.py) | 다익스트라 알고리즘은 가중치가 있는 그래프에서 시작 노드로부터 다른 모든 노드까지의 최단 경로를 찾는 알고리즘입니다. |작성 예정 | 최단 경로 찾기 |
| [fibonacci_recursion.py](Algorithm_with_DataStructure/fibonacci_recursion.py) | 피보나치 수열을 재귀를 사용하여 구현한 코드입니다. | O(2^n) | 수열, 재귀 연습 |
| [fibonacci_recursion_memoization.py](Algorithm_with_DataStructure/fibonacci_recursion_memoization.py) | 피보나치 수열을 메모이제이션을 사용하여 최적화한 코드입니다. | O(n) | 수열, 동적 프로그래밍 연습 |
| [combination_generation.py](Algorithm_with_DataStructure/combination_generation.py) | 주어진 리스트에서 n개의 원소를 선택하는 모든 가능한 조합을 생성합니다. |작성 예정 | 데이터 분석, 통계학에서 조합의 경우의 수를 구할 때 사용 |
| [dfs_recursion.py](Algorithm_with_DataStructure/dfs_recursion.py) | 그래프나 트리를 깊이 우선 탐색하는 알고리즘입니다. 이 코드는 재귀를 사용하여 구현되었습니다. |작성 예정 | 그래프 탐색, 경로 찾기 |
| [dfs_stack.py](Algorithm_with_DataStructure/dfs_stack.py) | 그래프나 트리를 깊이 우선 탐색하는 알고리즘입니다. 이 코드는 스택을 사용하여 구현되었습니다. |작성 예정 | 그래프 탐색, 경로 찾기 |
| [dijkstra.py](Algorithm_with_DataStructure/dijkstra.py) | 시작 노드로부터 그래프 내의 다른 모든 노드까지의 최단 경로를 찾는 알고리즘입니다. |작성 예정 | 최단 경로 찾기 |
| [fibonacci_recursion.py](Algorithm_with_DataStructure/fibonacci_recursion.py) | 피보나치 수열을 재귀를 사용하여 계산합니다. | O(2^n) | 수열, 재귀 연습 |
| [fibonacci_recursion_memoization.py](Algorithm_with_DataStructure/fibonacci_recursion_memoization.py) | 피보나치 수열을 메모이제이션을 사용하여 최적화하여 계산합니다. | O(n) | 수열, 동적 프로그래밍 연습 |
| [interval_sum.py](Algorithm_with_DataStructure/interval_sum.py) | 주어진 리스트의 연속된 부분 리스트의 합 중에서 가장 큰 값을 찾는 알고리즘입니다. |작성 예정 | 최대 부분 배열 문제 |
| [list_element_sum.py](Algorithm_with_DataStructure/list_element_sum.py) | 리스트의 모든 원소의 합을 계산합니다. |작성 예정 | 리스트 연산 |
| [merge_list_to_dictionary.py](Algorithm_with_DataStructure/merge_list_to_dictionary.py) | 두 개의 리스트를 병합하여 사전 형태로 반환합니다. |작성 예정 | 데이터 구조 변환 |
| [permutation_generation.py](Algorithm_with_DataStructure/permutation_generation.py) | 주어진 리스트의 원소로 만들 수 있는 모든 순열을 생성합니다. |작성 예정 | 데이터 분석, 순열의 경우의 수 계산 |
| [prime_number_detection.py](Algorithm_with_DataStructure/prime_number_detection.py) | 주어진 숫자가 소수인지 판별합니다. |작성 예정 | 수학 문제, 암호화 |
| [priority_queue.py](Algorithm_with_DataStructure/priority_queue.py) | 우선순위 큐를 구현하고 사용하는 방법을 보여줍니다. |작성 예정 | 데이터 처리, 작업 스케줄링 |
| [queue.py](Algorithm_with_DataStructure/queue.py) | 큐(Queue) 데이터 구조를 구현하고 사용하는 방법을 보여줍니다. |작성 예정 | 데이터 처리, 작업 스케줄링 |
| [remove_duplicates.py](Algorithm_with_DataStructure/remove_duplicates.py) | 리스트에서 중복된 원소를 제거합니다. |작성 예정 | 데이터 정리 |
| [stack.py](Algorithm_with_DataStructure/stack.py) | 스택(Stack) 데이터 구현하고 사용하는 방법을 보여줍니다. |작성 예정 | 데이터 처리, 작업 스케줄링 |

## 기여 방법

이 프로젝트에 기여하고 싶으신 분들은 Pull Request를 통해 기여할 수 있습니다.

