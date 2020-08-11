if __name__ == "__main__":

    # 입력력
    N = int(input())

    # DP 초기화
    dp = [0] * 1001

    # dp
    dp[1], dp[2] = 1, 3
    for i in range(3, N + 1):
        dp[i] = (dp[i - 2] * 2 + dp[i - 1]) % 796796

    # 출력
    print(dp[N])