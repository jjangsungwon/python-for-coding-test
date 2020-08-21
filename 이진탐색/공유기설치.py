if __name__ == "__main__":
    n, c = map(int, input().split())  # 집의 개수, 공유기의 개수
    array = [int(input()) for _ in range(n)]

    # 이분 탐색을 하기 위해서 오름차순 정렬
    array.sort()

    # left, right 초기화(거리의 가능한 경우)
    left, right = 1, max(array) - min(array)

    # 이분 탐색
    max_length = -1
    while left <= right:
        mid = (left + right) // 2
        index, cnt = 0, 1

        for i in range(1, len(array)):
            if array[i] - array[index] >= mid:
                cnt += 1
                index = i

        if cnt >= c:
            left = mid + 1
            max_length = max(max_length, mid)
        elif cnt < c:  # 거리를 좁힐 필요가 있다.
            right = mid - 1

    # 출력
    print(max_length)
