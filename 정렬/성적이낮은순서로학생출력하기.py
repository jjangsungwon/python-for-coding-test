if __name__ == "__main__":
    N = int(input())
    score = [list(map(str, input().split())) for _ in range(N)]

    # 점수 int형 변환(str -> int)
    for i in range(N):
        score[i][1] = int(score[i][1])

    # 점수를 기준으로 내림차순 정렬
    score = sorted(score, key=lambda k : k[1])

    # 출력
    for i in range(N):
        print(score[i][0], end=" ")