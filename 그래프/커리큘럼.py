from collections import deque
import copy


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])


if __name__ == "__main__":
    # 노드의 개수 입력받기
    v = int(input())

    # 진입차수 0으로 초기화
    indegree = [0] * (v + 1)

    # 그래프 초기화
    graph = [[] for _ in range(v + 1)]

    # 각 강의 시간 초기화
    time = [0] * (v + 1)

    # 간선 정보 입력받기
    for i in range(1, v + 1):
        data = list(map(int, input().split()))
        time[i] = data.pop(0)
        for x in data:
            if x == -1:
                break
            indegree[i] += 1
            graph[x].append(i)

    topology_sort()

