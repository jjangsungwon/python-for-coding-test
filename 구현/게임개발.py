# 상, 좌, 하, 우 (왼쪽 방향으로)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def turn_left():
    global d
    d = (d + 1) % 4


def simulation():
    global x, y
    visited = set()
    visited.add((x, y))
    count = 1
    rotation = 0

    while True:
        # 왼쪽으로 회전
        turn_left()
        nx = x + dx[d]
        ny = y + dy[d]

        if arr[nx][ny] == 0 and (nx, ny) not in visited:
            x, y = nx, ny
            visited.add((x, y))
            count += 1
            rotation = 0
        else:
            rotation += 1

        if rotation == 4:  # 이동할 곳이 없으면
            nx, ny = x - dx[d], y - dy[d]
            if arr[nx][ny] == 1:
                break
            else:
                x, y = nx, ny
            rotation = 0

    return count


if __name__ == "__main__":
    # 입력
    N, M = map(int, input().split())
    x, y, d = map(int, input().split())  # (현재 위치), 방향
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(simulation())
