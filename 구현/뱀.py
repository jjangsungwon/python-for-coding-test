def move(snack, dir):  # 뱀의 이동
    if dir == 1:  # 상
        snack.insert(0, [snack[0][0] - 1, snack[0][1]])
    elif dir == 2:  # 우
        snack.insert(0, [snack[0][0], snack[0][1] + 1])
    elif dir == 3:  # 하
        snack.insert(0, [snack[0][0] + 1, snack[0][1]])
    else:  # 좌
        snack.insert(0, [snack[0][0], snack[0][1] - 1])


def direction_change(snack, direction, dir):
    if direction == "D":
        return dir % 4 + 1
    else:
        if dir == 1:
            return 4
        else:
            return dir - 1


if __name__ == "__main__":
    # 입력
    N = int(input())  # 보드의 크기
    array = [[0] * N for _ in range(N)]  # 맵 초기화
    K = int(input())  # 사과의 크기
    for _ in range(K):
        r, c = map(int, input().split())
        array[r - 1][c - 1] = 1  # 사과 정보 저장
    L = int(input())  # 뱀의 방향 변환 횟수
    change = []  # 뱀의 방향 변환 정보 저장
    for _ in range(L):
        time, direction = input().split()
        change.append((int(time), direction))

    # 1 - 상, 2 - 우, 3 - 하, 4 - 좌 방향
    snack = [[0, 0]]  # 머리
    dir = 2  # 방향
    time = 0
    while True:
        move(snack, dir)  # 머리 이동
        time += 1
        # 자기 몸에 닿인 경우
        for i in range(1, len(snack)):
            if [snack[0][0], snack[0][1]] == [snack[i][0], snack[i][1]]:
                print(time)
                exit(0)

        if snack[0][0] < 0 or snack[0][0] >= N or snack[0][1] < 0 or snack[0][1] >= N:  # 벽을 만나는 경우
            break

        # 사과 여부 확인
        if array[snack[0][0]][snack[0][1]] == 1:  # 사과가 있다면
            array[snack[0][0]][snack[0][1]] = 0  # 사과 제거
            pass  # 꼬리 변동 x
        else:
            snack.pop()

        # 방향 전환 여부 확인
        if len(change) >= 1 and change[0][0] == time:
            t, direction = change.pop(0)
            dir = direction_change(snack, direction, dir)
    print(time)