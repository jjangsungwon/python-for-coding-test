if __name__ == "__main__":
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    # 각 무게에 해당하는 볼링공의 개수 카운트
    count = [0] * 11
    for value in data:
        count[value] += 1

    # 1부터 M까지의 각 무게에 대하여 처리
    answer = 0
    for i in range(1, M + 1):
        N -= count[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
        answer += count[i] * N

    # 출력
    print(answer)