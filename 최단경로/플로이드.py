import sys


if __name__ == "__main__":

    # 입력
    n = int(input())  # 도시의 개수
    m = int(input())  # 버스의 개수
    connect = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        connect[a][b] = min(connect[a][b], c)  # a에서 b로 가는데 필요한 비용 값
    for i in range(n + 1):
        connect[i][i] = 0  # 자기 자신에게 가는 비용 값 0으로 수정

    # 플로이드-워셜
    for k in range(1, n + 1):  # k -> j로 가는 경로의 최솟값 탐색
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                connect[i][j] = min(connect[i][j], connect[i][k] + connect[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if connect[i][j] == sys.maxsize:
                connect[i][j] = 0

    for i in range(1, n + 1):
        print(" ".join(map(str, connect[i][1:])))