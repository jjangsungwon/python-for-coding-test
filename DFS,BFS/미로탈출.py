from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque([[0, 0, 1]])  # 위치와 이동 횟수 정보 저장

    while queue:
        x, y, cnt = queue.popleft()
        if x == N - 1 and y == M - 1:  # 목표 지점 도달
            return cnt
        else:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if arr[nx][ny] == 0:
                    continue
                if arr[nx][ny] == 1 and (nx, ny) != (0, 0):  # 해당 노드를 처음 방문 하는 경우에만 최단 거리 기록, 시작점 제외
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append([nx, ny, cnt + 1])


if __name__ == "__main__":

    # 입력
    N, M = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    # BFS 탐색
    print(bfs())
