import heapq


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, - 1, 1]
INF = 1e9


def dijkstra():
    q = []
    heapq.heappush(q, [0, 0, array[0][0]])  # 위치, 에너지 소묘량
    w = [[INF] * n for _ in range(n)]  # 이동 에너지 소모량 저장 배열
    while q:  # 큐가 빌 때까지 진행
        x, y, weight = heapq.heappop(q)
        if weight > w[x][y]:  # 이미 더 좋은 경우로 처리된 상황
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:  # 범위 체크
                if weight + array[nx][ny] <= w[nx][ny]:  # 저장된 에너지 소모량보다 적게 도달 할 수 있다면 업데이트
                    w[nx][ny] = weight + array[nx][ny]
                    heapq.heappush(q, [nx, ny, w[nx][ny]])
    return w[n - 1][n - 1]


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())  # 탐사 공간의 크기
        array = [list(map(int, input().split())) for _ in range(n)]

        # 다익스트라
        print(dijkstra())
