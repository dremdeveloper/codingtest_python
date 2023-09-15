#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

# "guard clauses"는 특정 조건이 충족되지 않을 때 함수나 루프를 조기에 종료하는 코드 패턴입니다.
# 이 패턴은 중첩을 줄이고 코드의 가독성을 높이기 위해 사용됩니다. 
# 일반적으로 "guard clauses"는 함수의 시작 부분에 위치하며, 특정 조건이 충족되지 않을 때 
# 함수를 조기에 종료(early exit)하는 방법을 제공합니다.

def process_data(data):
    # data가 리스트가 아니라면, 함수를 조기에 종료한다.
    if not isinstance(data, list):
        return "Invalid data type"

    # data가 비어 있지 않다면, 처리를 계속한다.
    if not data:
        return "Data cannot be empty"

    # data를 처리하고 결과를 반환한다.
    result = [item * 2 for item in data]
    return result

# 예제 사용법
data_input = [1, 2, 3, 4, 5]
print(process_data(data_input))  # 출력: [2, 4, 6, 8, 10] (정상적인 처리)

invalid_input = "test"
print(process_data(invalid_input))  # 출력: "Invalid data type" (데이터 타입이 잘못됨)

empty_input = []
print(process_data(empty_input))  # 출력: "Data cannot be empty" (데이터가 비어 있음)
