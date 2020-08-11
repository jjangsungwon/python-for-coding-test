import sys


if __name__ == "__main__":
    N, M = map(int, input().split())
    coin = [int(input()) for _ in range(N)]

    dp = [sys.maxsize] * (M + 1)

    # coin에 들어있는 값은 1개로 가능
    for i in range(N):
        if coin[i] > M:
            continue
        else:
            dp[coin[i]] = 1

    # dp
    for i in range(1, M + 1):
        for j in range(N):
            if i + coin[j] <= M:
                dp[i + coin[j]] = min(dp[i] + 1, dp[i + coin[j]])

    if dp[M] == sys.maxsize:
        print(-1)
    else:
        print(dp[M])