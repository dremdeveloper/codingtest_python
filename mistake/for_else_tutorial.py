#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 주어진 숫자 리스트에서 특정 숫자를 찾는 예제

numbers = [1, 3, 5, 7, 9]
target_number = 4

for number in numbers:
    if number == target_number:
        print(f"Found {target_number}!")
        break
else:
    # for 루프가 중간에 break 되지 않고 완전히 실행되면 else 블록이 실행됩니다.
    print(f"{target_number} was not found in the list.")

# 위의 코드에서는 4가 리스트에 없으므로 "4 was not found in the list."가 출력됩니다.

# 실수 예: else 블록을 for 루프가 항상 실행되는 마지막 부분으로 잘못 이해하는 경우
# 다음과 같은 잘못된 코드를 작성할 수 있습니다.

# target_number = 5

# for number in numbers:
#     if number == target_number:
#         print(f"Found {target_number}!")
#     else:
#         # 이 else 블록은 for 루프의 각 반복마다 실행됩니다.
#         print(f"{target_number} was not found in the list.")

# 위의 코드는 5 이외의 모든 숫자에 대해 "5 was not found in the list."를 출력합니다.

# 올바른 사용법: for-else를 사용하여 리스트에서 특정 숫자를 찾고 결과를 출력합니다.

target_number = 7

for number in numbers:
    if number == target_number:
        print(f"Found {target_number}!")
        break
else:
    print(f"{target_number} was not found in the list.")

# 위의 코드에서는 7이 리스트에 있으므로 "Found 7!"이 출력됩니다.
