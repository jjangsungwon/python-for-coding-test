if __name__ == "__main__":
    t = int(input())  # 테스트 케이스의 개수

    # 테스트 케이스 실행
    for _ in range(t):
        n, m = map(int, input().split())
        array = []  # 금광 정보 리스트

        # 1차원 배열을 n * m 형태로 변환
        data = list(map(int, input().split()))
        for i in range(n):
            array.append(data[i * m:(i + 1) * m])

        # dynamic programming
        dp = [[0] * m for _ in range(n)]  # dp 배열
        # 첫 열
        for i in range(n):
            dp[i][0] = array[i][0]
        for i in range(1, m):
            for j in range(n):
                # 왼쪽
                dp[j][i] = max(dp[j][i], dp[j][i - 1] + array[j][i])
                # 왼쪽 위
                if j - 1 >= 0:
                    dp[j][i] = max(dp[j][i], dp[j - 1][i - 1] + array[j][i])
                # 왼쪽 아래
                if j + 1 < n:
                    dp[j][i] = max(dp[j][i], dp[j + 1][i - 1] + array[j][i])

        # 최댓값 출력
        answer = 0
        for i in range(n):
            answer = max(answer, dp[i][m - 1])

        print(answer)