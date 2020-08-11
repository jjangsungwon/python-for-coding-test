INF = int(1e9)


if __name__ == "__main__":

    # 회사의 개수(N)와 경로의 개수(M) 입력
    N, M = map(int, input().split())

    # 거리값 초기화
    distance = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        distance[i][i] = 0  # 자기 자신

    # 회사 연결 입력
    for _ in range(M):
        a, b = map(int, input().split())
        distance[a][b] = 1  # 연결
        distance[b][a] = 1  # 양방향

    X, K = map(int, input().split())

    # 플로이드-워셜(Floyd-Warshall)
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    # K를 지나고 X를 가는 거리
    answer = distance[1][K] + distance[K][X]

    # 출력
    if answer >= INF:
        print(-1)
    else:
        print(answer)
