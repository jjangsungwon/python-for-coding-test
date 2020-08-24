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

    n, m = map(int, input().split())  # 집의 수, 도로의 수 입력

    # parent 초기화
    parent = [0] * n
    for i in range(n):
        parent[i] = i  # 처음에는 자기 자신을 가리키도록 한다.

    # 도로 정보
    total = 0
    q = []
    for _ in range(m):
        a, b, cost = map(int, input().split())
        heapq.heappush(q, (cost, a, b))  # 크루스칼을 편리하게 구현하기 위해 우선순위 큐를 활용하였다.
        total += cost

    # 가중치가 가장 작은 간선부터 삽입한다.
    answer = 0
    for i in range(m):
        cost, a, b = heapq.heappop(q)
        if find_parent(a) == find_parent(b):  # 사이클이면 건너뛴다.
            continue
        else:
            answer += cost
            union_parent(a, b)

    print(total - answer)

