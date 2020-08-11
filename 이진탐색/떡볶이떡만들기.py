if __name__ == "__main__":

    # 입력
    N, M = map(int, input().split())
    array = list(map(int, input().split()))

    # 이진 탐색 초기값, max(array)보다 큰 절단기의 높이는 의미가 없다.
    left, right = 0, max(array)
    max_height = -1

    # 이진 탐색을 하기 위해서 정렬
    array.sort()

    # 이진 탐색
    while left <= right:
        mid = (left + right) // 2
        temp = 0

        # 해당 높이로 손님에게 줄 수 있는 떡의 길이 파악
        for i in range(N):
            if array[i] > mid:
                temp += array[i] - mid

        # 해당 높이로 M이상을 줄 수 있을때(높이를 더 높여본다)
        if temp >= M:
            max_height = max(max_height, mid)
            left = mid + 1
        else:
            right = mid - 1

    # 출력
    print(max_height)