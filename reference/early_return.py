#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# Early return은 조건에 따라 함수에서 빠르게 반환하여 불필요한 실행을 방지하는 코드 패턴입니다.
# 이는 함수의 로직을 더욱 명확하게 만들고, 중첩된 조건문을 줄일 수 있습니다.

def find_item(items, target):
    for item in items:
        if item == target:
            return f"Item '{target}' found!"
    # 만약 target 아이템을 찾지 못했다면, 이 문장이 실행됩니다.
    return f"Item '{target}' not found"

# 예시
items_list = ["apple", "banana", "cherry"]
print(find_item(items_list, "banana"))  # 출력: "Item 'banana' found!"
print(find_item(items_list, "grape"))  # 출력: "Item 'grape' not found"
