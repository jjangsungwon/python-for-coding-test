import heapq


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    n = int(input())  # 행성의 개수
    x, y, z = [], [], []
    for i in range(n):
        data = list(map(int, input().split()))
        x.append((data[0], i))
        y.append((data[1], i))
        z.append((data[2], i))

    x.sort()
    y.sort()
    z.sort()

    # 부모 배열 초기화
    parent = [0] * n
    for i in range(n):
        parent[i] = i

    # 좌표 사이의 거리 계산
    q = []
    for i in range(n - 1):
        heapq.heappush(q, (x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
        heapq.heappush(q, (y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
        heapq.heappush(q, (z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

    # 크루스칼 - 가장 작은 값부터 삽입
    answer = 0
    for i in range(len(q)):
        cost, x, y = heapq.heappop(q)
        if find_parent(x) != find_parent(y):  # 사이클
            union_parent(x, y)
            answer += cost

    # 출력
    print(answer)