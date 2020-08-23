import copy


if __name__ == "__main__":
    n = int(input())  # 병사의 수
    array = list(map(int, input().split()))

    # dp 배열 초기화, 최솟값 초기화
    dp = [1] * n

    # dp, 가장 긴 감소하는 부분 수열을 찾고 전체 길이에서 뺀다.
    for i in range(n):
        for j in range(i):
            if array[i] < array[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(n - max(dp))