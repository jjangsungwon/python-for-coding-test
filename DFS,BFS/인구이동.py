from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(row, col):
    bfs_flag = False  # 인구 이동 발생 여부

    result = [(row, col)]  # 인구 이동이 일어날 칸 정보 저장
    q = deque()
    q.append((row, col))
    visited = set()
    visited.add((row, col))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if l <= abs(array[x][y] - array[nx][ny]) <= r and (nx, ny) not in visited:
                    q.append((nx, ny))
                    result.append((nx, ny))
                    visited.add((nx, ny))
                    bfs_flag = True
    return bfs_flag, result


if __name__ == "__main__":
    n, l, r = map(int, input().split())  # 나라 개수, 이동 제한 최소 값, 이동 제한 최대 값 입력
    array = [list(map(int, input().split())) for _ in range(n)]

    count = 0  # 총 인구 이동 횟수
    pre_count = 0
    while True:
        calcul = []
        pre_count = count
        for i in range(n):
            for j in range(n):
                flag, temp = bfs(i, j)
                if flag:
                    calcul.append(temp)

        if len(calcul) == 0:
            break
        else:
            for i in range(len(calcul)):
                total = 0
                # 대입할 값 계산
                for j in range(len(calcul[i])):
                    total += array[calcul[i][j][0]][calcul[i][j][1]]
                value = total // len(calcul[i])
                # 값 대입
                for j in range(len(calcul[i])):
                    array[calcul[i][j][0]][calcul[i][j][1]] = value
            count += 1
    # 출력
    print(count)
