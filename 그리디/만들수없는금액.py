if __name__ == "__main__":
    N = int(input())
    coin = list(map(int, input().split()))

    # 동전 올림차순 정렬
    coin.sort()

    # 금액의 크기를 점차 늘이는 방법으로 만들 수 없는 금액의 최솟값 구현
    answer = 1  # 초기값
    for i in range(len(coin)):
        if coin[i] <= answer:
            answer += coin[i]
        else:
            break

    # 출력
    print(answer)
