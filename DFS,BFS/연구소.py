from itertools import permutations
from collections import deque
import copy

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(arr):
    q = deque()
    visited = []
    for v in virus:
        q.append(v)
    while q:  # 큐가 빌 때까지
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and (nx, ny) not in visited:
                    arr[nx][ny] = 2  # 바이러스 전파
                    visited.append((nx, ny))
                    q.append((nx, ny))


def safe_area(arr):
    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                count += 1
    return count


if __name__ == "__main__":

    n, m = map(int, input().split())  # 행, 열 입력
    array = [list(map(int, input().split())) for _ in range(n)]  # 맵 입력

    # 벽을 설치할 수 있는 후보 찾기(빈칸 - 0)
    wall = []
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                wall.append((i, j))

    # 바이러스 리스트
    virus = []
    for i in range(n):
        for j in range(m):
            if array[i][j] == 2:
                virus.append((i, j))

    # 벽 3개를 설치하는 모든 경우에 대해서 탐색 시작
    answer = 0
    for data in list(permutations(wall, 3)):
        copy_array = copy.deepcopy(array)
        for row, col in data:
            copy_array[row][col] = 1  # 벽 설치
        bfs(copy_array)  # 바이러스 전파
        answer = max(answer, safe_area(copy_array))

    # 출력
    print(answer)
