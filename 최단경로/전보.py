import heapq


INF = int(1e9)


def dijkstra(start):
    distance[start] = 0  # 시작 지점
    q = []
    heapq.heappush(q, (0, start))  # (거리, 노드번호)
    while q:  # 큐가 비어있지 않다면
        dist, loc = heapq.heappop(q)
        if distance[loc] < dist:  # 최솟값만 사용하기 위해서
            continue
        for temp in graph[loc]:
            cost = dist + temp[1]
            if cost < distance[temp[0]]:
                distance[temp[0]] = cost
                heapq.heappush(q, (cost, temp[0]))


if __name__ == "__main__":

    # 입력
    N, M, C = map(int, input().split())

    # 노드 갯수에 해당하는 그래프 형태 초기화
    graph = [[] for _ in range(N + 1)]

    # 통로에 대한 정보 입력
    for _ in range(M):
        X, Y, Z = map(int, input().split())
        graph[X].append((Y, Z))

    # 노드 거리 정보
    distance = [INF] * (N + 1)

    # 다익스트라
    dijkstra(C)

    # 결괏값 계산
    count = 0
    t = 0
    for i in range(1, N + 1):
        if distance[i] != INF and i != C:
            count += 1
            t = max(t, distance[i])

    # 출력
    print(count, t)