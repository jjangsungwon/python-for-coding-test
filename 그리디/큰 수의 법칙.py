if __name__ == "__main__":
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))

    # 내림차순 정렬
    data.sort(reverse=True)

    # 가장 큰 수가 2개 이상인 경우
    total = 0
    if data[0] == data[1]:
        total = data[0] * M
    else:  # 가장 큰 수가 1개인 경우
        for i in range(1, M + 1):
            if i % K == 0:  # K개 사용한 경우
                total += data[1]
            else:
                total += data[0]
    print(total)