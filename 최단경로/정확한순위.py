INF = int(1e9)


if __name__ == "__main__":

    # 입력
    n, m = map(int, input().split())  # 학생들의 수, 두 학생읭 성적을 비교한 횟수
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1  # 경로 추가
    for i in range(1, n + 1):
        graph[i][i] = 1  # 자기 자신으로 가는 길은 있다고 가정

    # 플로이드-워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] == 1:
                    continue
                else:
                    if graph[i][k] + graph[k][j] == 2:  # 경로가 있으면
                        graph[i][j] = 1

    # 1부터 차례대로 순위 확인이 가능한지 체크
    answer = 0
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if graph[i][j] == 1 or graph[j][i] == 1:
                count += 1
        if count == n:
            answer += 1

    # 출력
    print(answer)

