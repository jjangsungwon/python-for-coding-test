from itertools import permutations

INF = 1e9

if __name__ == "__main__":
    n = int(input())  # 수의 개수
    numbers = list(map(int, input().split()))  # 연산 대상
    operation = list(map(int, input().split()))  # 연산자

    max_value = -INF  # 최댓값
    min_value = INF  # 최솟값

    # operation을 순열에 대입할 수 있는 형태로 변환
    oper = ['+', '-', '*', '//']
    temp = []
    for i in range(len(operation)):
        for j in range(operation[i]):
            temp.append(oper[i])

    # 연산자를 numbers에 넣을 수 있는 모든 경우의 수를 대입하면서 최솟값, 최댓값을 찾아낸다.
    for data in list(permutations(temp, n - 1)):
        value = numbers[0]
        for i in range(n - 1):
            if data[i] == "+":
                value += numbers[i + 1]
            elif data[i] == "-":
                value -= numbers[i + 1]
            elif data[i] == "*":
                value *= numbers[i + 1]
            elif data[i] == "//":
                if value < 0:
                    value = -((-value) // numbers[i + 1])
                else:
                    value //= numbers[i + 1]
        max_value = max(max_value, value)
        min_value = min(min_value, value)

    # 출력
    print(max_value)
    print(min_value)