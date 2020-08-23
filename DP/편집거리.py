if __name__ == "__main__":

    # 입력
    original = list(input())
    target = list(input())

    original_length = len(original)
    target_length = len(target)

    # 2차원 dp 초기화
    dp = [[0] * (target_length + 1) for _ in range(original_length + 1)]

    # 1행과 1열 초기화
    for i in range(original_length + 1):
        dp[i][0] = i
    for i in range(target_length + 1):
        dp[0][i] = i

    # dp 탐색 시작
    for i in range(1, original_length + 1):
        for j in range(1, target_length + 1):
            if original[i - 1] == target[j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    print(dp[original_length][target_length])