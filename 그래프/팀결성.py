def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 경로 압축
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:  # 작은 값이 부모
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":

    # 입력
    N, M = map(int, input().split())

    # 자기 자신을 가르키도록 설정
    parent = [i for i in range(N + 1)]

    # 연산 입력
    for _ in range(M):
        f, a, b = map(int, input().split())
        if f == 1:  # 같은 팀 여부 확인
            if find_parent(parent, a) == find_parent(parent, b):
                print("YES")
            else:
                print("NO")
        else:  # 팀 합치기
            union_parent(parent, a, b)