from itertools import combinations
import copy


def search(arr):  # 선생님 감시 진행
    for k in range(len(teacher)):
        row, col = teacher[k]
        # 상
        for i in range(row - 1, -1, -1):
            if arr[i][col] == "O":
                break
            else:
                arr[i][col] = "T"
        # 하
        for i in range(row + 1, n):
            if arr[i][col] == "O":
                break
            else:
                arr[i][col] = "T"
        # 좌
        for i in range(col - 1, -1, -1):
            if arr[row][i] == "O":
                break
            else:
                arr[row][i] = "T"
        # 우
        for i in range(col + 1, n):
            if arr[row][i] == "O":
                break
            else:
                arr[row][i] = "T"


def student_count(arr):  # 학생 수 계산
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "S":
                count += 1
    return count


if __name__ == "__main__":
    n = int(input())  # 맵의 크기
    array = [list(input().split()) for _ in range(n)]  # 복도 정보

    # 빈칸 및 선생님 정보 저장
    blank = []
    teacher = []
    stu_count = 0
    for i in range(n):
        for j in range(n):
            if array[i][j] == "X":
                blank.append((i, j))
            elif array[i][j] == "T":
                teacher.append((i, j))
            elif array[i][j] == "S":
                stu_count += 1  # 학생 수

    # 빈칸 중에 3개를 고르는 모든 경우의 수를 탐색한다.
    for data in list(combinations(blank, 3)):
        temp = copy.deepcopy(array)
        for i in range(3):
            temp[data[i][0]][data[i][1]] = "O"  # 장애물 설치
        # 선생님 감시 진행
        search(temp)
        if stu_count == student_count(temp):  # 감시를 피할 수 있는 경우
            print("YES")
            exit(0)
    print("NO")