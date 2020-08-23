if __name__ == "__main__":
    n = int(input())  # 삼각형의 크기
    array = [list(map(int, input().split())) for _ in range(n)]

    # dynamic programming
    for i in range(1, n):
        for j in range(len(array[i])):
            # 오른쪽 위만 존재
            if j == 0:
                array[i][j] += array[i - 1][j]
            elif j == len(array[i]) - 1:  # 왼쪽 위만 존재
                array[i][j] += array[i - 1][j - 1]
            else:  # 모두 존재
                array[i][j] += max(array[i - 1][j], array[i - 1][j - 1])

    # 출력
    answer = max(array[n - 1])
    print(answer)
