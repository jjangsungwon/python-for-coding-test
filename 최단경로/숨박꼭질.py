import heapq


INF = 1e9


def dijkstra():
    q = []
    distance = [INF] * (n + 1)
    distance[1] = 1
    # 가는 길이 있는 값은 처음에 대입합니다.
    for index in graph[1]:
        distance[index] = 1
        heapq.heappush(q, [1, index])  # 거리, 인덱스값을 우선순위 큐에 삽입합니다.

    while q:  # 큐가 빌 때까지 진행합니다.
        d, index = heapq.heappop(q)
        if distance[index] < d:  # 이미 더 좋은 상황으로 처리한 경우에는 무시합니다.
            continue
        for value in graph[index]:
            if d + 1 < distance[value]:
                distance[value] = d + 1
                heapq.heappush(q, [d + 1, value])

    # 가장 거리가 긴 값, 인덱스, 개수 파악
    max_length, index, count = -1, -1, 0
    for i in range(len(distance)):
        if distance[i] != INF:
            max_length = max(max_length, distance[i])
    index_flag = False
    for i in range(len(distance)):
        if max_length == distance[i] and not index_flag:
            index = i
            index_flag = True
            count += 1
        elif max_length == distance[i]:
            count += 1

    return index, max_length, count


if __name__ == "__main__":

    # 입력
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]  # 연결 그래프 초기화
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)  # 양방향 연결 추가
        graph[b].append(a)

    # 다익스트라 알고리즘 실행
    print(" ".join(map(str, dijkstra())))