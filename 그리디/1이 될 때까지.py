if __name__ == "__main__":
    N, K = map(int, input().split())

    # 1을 만들때까지 반복
    count = 0
    while N != 1:
        if N % K != 0:  # K로 나누어 떨어질 때까지 -1 연산 수행
            N -= 1
        else:
            N //= K  # 나누어 떨어지면 나누기 연산 수행
        count += 1

    # 출력
    print(count)