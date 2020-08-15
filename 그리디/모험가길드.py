if __name__ == "__main__":

    # 입력
    N = int(input())
    array = list(map(int, input().split()))

    # 최대한 많은 그룹을 만들기 위해서 공포도가 낮은 값부터 그룹을 형성
    array.sort()
    answer = 0  # 그룹 갯수
    count = 1
    for i in range(N):
        if array[i] <= count:
            answer += 1
            count = 1
        else:
            count += 1

    # 출력
    print(answer)
