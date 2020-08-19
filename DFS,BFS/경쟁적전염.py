import heapq
import copy


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
if __name__ == "__main__":
    n, k = map(int, input().split())  # 맵의 크기, 바이러스 종류 갯수 입력
    array = [list(map(int, input().split())) for _ in range(n)]  # 맵 초기화
    s, x, y = map(int, input().split())  # 종료 시간, (x, y)위치 좌표 입력

    q = []  # 바이러스 리스트 - 우선 순위 큐를 활용하여 바이러스 값이 낮은 값 부터 파악하는게 편리하도록 구현하였다.
    for i in range(n):
        for j in range(n):
            if array[i][j] != 0:  # 바이러스
                heapq.heappush(q, (array[i][j], i, j))  # 바이러스 종류, 위치 삽입

    time = 1
    while time <= s:  # s초까지 반복문 진행
        temp = []
        while q:
            dim, row, col = heapq.heappop(q)
            for i in range(4):
                nx, ny = row + dx[i], col + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if array[nx][ny] == 0:
                        array[nx][ny] = dim
                        heapq.heappush(temp, (dim, nx, ny))
        time += 1
        q = copy.deepcopy(temp)

    # 출력
    print(array[x - 1][y - 1])