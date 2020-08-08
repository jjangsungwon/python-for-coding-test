if __name__ == "__main__":
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 각 행 내림차순 정렬
    for i in range(N):
        data[i].sort()

    # 탐색
    max_value = -1
    for i in range(N):
        if max_value < data[i][0]:
            max_value = data[i][0]

    # 출력
    print(max_value)