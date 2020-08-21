# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메소드
def count_by_value(array, x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n - 1)

    # 수열에 x가 존재하지 않는 경우
    if a == -1:
        return -1

    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n - 1)

    # 개수를 반환
    return b - a + 1


def first(array, x, left, right):
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            flag = True
            break

        if array[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    if not flag:
        return -1

    answer = mid
    for i in range(mid - 1, -1, -1):
        if array[i] == x:
            answer = i
    return answer


def last(array, x, left, right):
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            flag = True
            break

        if array[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    if not flag:
        return -1

    answer = mid
    for i in range(mid + 1, len(array)):
        if array[i] == x:
            answer = i
    return answer


if __name__ == "__main__":
    n, x = map(int, input().split())  # 숫자의 개수, 찾고자 하는 값
    array = list(map(int, input().split()))

    print(count_by_value(array, x))
