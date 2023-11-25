# ❶ 각 물건의 단위 무게당 가치를 계산하여 items 리스트에 추가
def calculate_unit_value(items):
  for item in items:
    item.append(item[1] / item[0])
  return items

# ❷ 단위 무게당 가치가 높은 순으로 물건을 정렬
def sort_by_unit_value(items):
  items.sort(key=lambda x: x[2], reverse=True)
  return items


def knapsack(items, weight_limit):
  total_value = 0  # ❸ 선택한 물건들의 총 가치를 저장하는 변수
  remaining_weight = weight_limit  # ❹ 남은 무게 한도를 저장하는 변수

  # ❺ 물건을 선택합니다.
  for item in items:
    if item[0] <= remaining_weight:
      # ❻ 남은 무게 한도 내에서 물건을 통째로 선택
      total_value += item[1]
      remaining_weight -= item[0]
    else:
      # ❼ 남은 무게 한도가 물건의 무게보다 작으면 쪼개서 일부분만 선택
      fraction = remaining_weight / item[0]
      total_value += item[1] * fraction
      break  # ❽ 이미 배낭의 무게 한도를 모두 사용한 경우,
  return total_value

def solution(items, weight_limit):
  items = calculate_unit_value(items)
  items = sort_by_unit_value(items)
  
  # ❾ 배낭의 무게 한도 내에서 담을 수 있는 물건들의 최대 가치를 반환
  return knapsack(items, weight_limit)  




# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([[10, 19], [7, 10], [6, 10]], 15)) # 반환값 : 273.33
# print(solution([[10, 60], [20, 100], [30, 120]], 50)) # 반환값 : 240
