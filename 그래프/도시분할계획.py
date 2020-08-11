def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":

    # 입력
    N, M = map(int, input().split())

    # 자기 자신을 가르키도록 설정
    parent = [i for i in range(N + 1)]

    # 간선 정보
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
        edges.append((c, b, a))

    # 정렬
    edges.sort()

    # 크루스칼
    answer = []
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) == find_parent(parent, b):
            continue
        else:
            union_parent(parent, a, b)
            answer.append(cost)

    # 가장 긴 간선 제거
    answer.pop(answer.index(max(answer)))
    print(sum(answer))


