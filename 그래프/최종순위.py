from collections import deque


def topological():
    q = deque()
    # 진입 차수가 0인 값 q에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 위상 정렬
    result = []
    for i in range(1, n + 1):
        if len(q) == 0:  # 사이클이 있는 경우
            return "IMPOSSIBLE"
        index = q.popleft()
        result.append(index)
        for j in range(1, n + 1):
            if graph[index][j]:  # index와 연결되어 있다면
                indegree[j] -= 1  # 진입 차수 감소
                if indegree[j] == 0:
                    q.append(j)
                    if len(q) >= 2:  # 결과가 2개 이상 가능한 경우(일관성이 없는 정보)
                        return "?"

    return " ".join(map(str, result))


if __name__ == "__main__":
    # 테스트 케이스의 개수만큼 반복
    for _ in range(int(input())):
        n = int(input())  # 팀의 수
        rank = list(map(int, input().split()))  # 작년 순위
        graph = [[False] * (n + 1) for _ in range(n + 1)]
        m = int(input())  # 순위 변동 수

        # 진입 차수
        indegree = [0] * (n + 1)

        # 자신보다 순위가 낮은 값 으로 연결(1등 -> 2등 -> 3등 ...)
        for i in range(n):
            for j in range(i + 1, n):
                graph[rank[i]][rank[j]] = True
                indegree[rank[j]] += 1

        # 순위 변동
        for _ in range(m):
            a, b = map(int, input().split())  # a가 b보다 높은 순위로 변동
            graph[b][a] = False  # 연걸 제거
            indegree[b] += 1  # 진입 차수 - 1
            graph[a][b] = True  # 연결 생성
            indegree[a] -= 1  # 진입 차수 + 1

        # 출력
        answer = topological()
        print(answer)
