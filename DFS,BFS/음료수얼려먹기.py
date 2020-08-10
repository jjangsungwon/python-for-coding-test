from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(row, col):
    global arr
    arr[row][col] = 1
    queue = deque([[row, col]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                queue.append([nx, ny])
                arr[nx][ny] = 1
            else:
                continue


if __name__ == "__main__":
    # 입력
    N, M = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    # bfs
    answer = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                bfs(i, j)
                answer += 1

    # 출력
    print(answer)