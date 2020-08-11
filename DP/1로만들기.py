if __name__ == "__main__":
    N = int(input())
    dp = [0] * (N + 1)

    # DP
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1
        if i % 5 == 0:  # 5로 나누어 떨어지는 경우
            dp[i] = min(dp[i], dp[i // 5] + 1)
        if i % 3 == 0:  # 3으로 나누어 떨어지는 경우
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0:  # 2로 나누어 떨어지는 경우
            dp[i] = min(dp[i], dp[i // 2] + 1)
    print(dp[N])
