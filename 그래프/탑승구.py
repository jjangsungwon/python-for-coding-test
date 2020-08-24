def find_parent(x):
    if x != parent[x]:
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
    # 입력
    g = int(input())  # 탑승구의 수
    p = int(input())  # 비행기의 수
    airplane = [int(input()) for _ in range(p)]

    # parent 초기화
    parent = [0] * (g + 1)
    for i in range(g + 1):
        parent[i] = i  # 처음에는 자기 자신을 부모로 가르키도록 한다.

    # airplane 원소를 하나씩 탐색하면서 도킹할 수 있는 비행기의 최대 개수 파악
    answer = 0
    for i in range(len(airplane)):
        index = find_parent(airplane[i])
        if index == 0:
            break
        else:
            union_parent(index, index - 1)  # index을 1칸 전이랑 연결한다.
            answer += 1
    # 출력
    print(answer)