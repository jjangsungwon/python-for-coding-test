if __name__ == "__main__":
    # 입력
    n = int(input())
    t, p = [], []
    for _ in range(n):
        i_t, i_p = map(int, input().split())
        t.append(i_t)
        p.append(i_p)

    # dp
    dp = [0] * n

    for i in range(n):
        if i + t[i] <= n:
            dp[i] = p[i]
            for j in range(i):
                if i >= j + t[j]:
                    dp[i] = max(dp[i], dp[j] + p[i])

    print(max(dp))