def binary_search(array, left, right):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    # 입력
    n = int(input())
    array = list(map(int, input().split()))

    # 이진 탐색
    answer = -1
    print(binary_search(array, 0, n - 1))

