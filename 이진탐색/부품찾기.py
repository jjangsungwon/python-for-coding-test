def binary_search(target, start, end):
    if start > end:
        return None
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:  # 일치
            return "yes"
        elif array[mid] > target:  # 중간값이 찾고자 하는 값보다 클 때
            end = mid - 1
        else:
            start = mid + 1
    return None  # 일치하는 값이 없을 때


if __name__ == "__main__":

    # 입력
    N = int(input())
    array = list(map(int, input().split()))
    M = int(input())
    find = list(map(int, input().split()))

    # 이진 탐색을 하기 위해서 정렬
    array.sort()

    # find에서 값을 하나씩 읽는다.
    for data in find:
        # 이진 탐색
        result = binary_search(data, 0, N - 1)
        if result is not None:
            print('yes', end=" ")
        else:
            print('no', end=" ")
