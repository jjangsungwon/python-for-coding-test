def rotation(arr):  # 시계 방햫으로 90도 회전
    length = len(arr)
    temp = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            temp[j][length - 1 - i] = arr[i][j]
    return temp


def check(arr):  # 자물쇠 해제 조건 확인
    length = len(arr) // 3
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if arr[i][j] != 1:
                return 0
    return 1


def solution(key, lock):
    length = len(lock)
    # lock 배열을 3배로 늘이기 (완전 탐색을 구현하기 위해서, 늘어난 부분은 0으로 채운다)
    for _ in range(length):  # 상, 하 추가
        lock = [[0] * length] + lock + [[0] * length]
    for i in range(len(lock)):  # 좌, 우 추가
        lock[i] = [0] * len(lock[i]) + lock[i] + [0] * len(lock[i])

    # 완전 탐색
    for k in range(4):
        key = rotation(key)
        for i in range(len(lock) - len(key) - 1):
            for j in range(len(lock) - len(key) - 1):
                for m in range(len(key)):
                    for n in range(len(key)):
                        lock[i + m][j + n] += key[m][n]
                if check(lock):
                    return True
                else:
                    for m in range(len(key)):
                        for n in range(len(key)):
                            lock[i + m][j + n] -= key[m][n]
    return False


if __name__ == "__main__":
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))