def find_parent(x):  # 의 parent 파악
    if x != parent[x]:
        x = find_parent(parent[x])
        return x
    else:
        return x


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a  # b의 부모를 a로 설정
    else:
        parent[a] = b


if __name__ == "__main__":

    # 입력
    n, m = map(int, input().split())  # 여행지의 수, 여행 계획에 속한 도시의 수
    graph = [list(map(int, input().split())) for _ in range(n)]
    move = list(map(int, input().split()))

    # 부모 노드 선언 및 초기화
    parent = [0] * n
    for i in range(n):
        parent[i] = i  # 자기 자신을 가르키도록 설정

    # 2차원 배열을 순회하면서 연결 정보가 있는 경우에 union 연산 실행
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                union_parent(i, j)

    # 여행이 가능한 지 파악
    for i in range(len(move) - 1):
        if find_parent(move[i]) == find_parent(move[i + 1]):
            continue
        else:
            print("NO")
            exit(0)
    print("YES")
