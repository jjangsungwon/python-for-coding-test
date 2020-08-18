import heapq
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0  # 시작 노드 거리 0
    while q:  # 큐가 비어 있지 않다면
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # 이미 처리된 값이라면 무시
            continue
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))


if __name__ == "__main__":

    n, m, k, x = map(int, input().split())  # 도시, 도로, 거리 정보, 출발 도시 번호 입력
    graph = [[] for _ in range(n + 1)]  # 노드 연결 관리
    visited = [False] * (n + 1)  # 방문 관리
    distance = [INF] * (n + 1)  # 거리 관리

    # 간선 입력
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append((b, 1))  # 거리 초기값 1

    # 다익스트라
    dijkstra(x)

    # 출력
    result = []
    for i in range(1, len(distance)):
        if distance[i] == k:
            result.append(i)
    if len(result) == 0:
        print(-1)
    else:
        for data in result:
            print(data)