from operator import itemgetter


def check(result):  # 현재 설치물이 조건을 만족하는지 확인
    for i in range(len(result)):
        x, y, a = result[i]
        if a == 0:  # 기둥
            if y == 0 or [x, y - 1, a] in result or [x, y, 1] in result or [x - 1, y, 1] in result:
                continue
            else:
                return False
        else:
            if [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result or ([x - 1, y, 1] in result and [x + 1, y, 1] in result):
                continue
            else:
                return False
    return True


def install(result, install_array):
    x, y, a = install_array
    if a == 0:  # 기둥
        if y == 0 or [x, y - 1, a] in result or [x, y, 1] in result or [x - 1, y, 1] in result:
            result.append(install_array)
    else:  # 보
        if [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result or ([x - 1, y, 1] in result and [x + 1, y, 1] in result):
            result.append(install_array)


def delete(result, delete_array):
    # 먼저 삭제 진행
    result.remove(delete_array)
    if not check(result):  # 조건을 만족하지 않으면
        result.append(delete_array)  # 다시 삽입


def solution(build_frame):
    result = []  # 최종 결과 리스트

    # build_frame의 값을 하나씩 읽어오면서 설치 및 삭제 진행
    for i in range(len(build_frame)):
        if build_frame[i][3] == 0:  # 삭제
            delete(result, build_frame[i][:3])
        else:  # 설치
            install(result, build_frame[i][:3])

    # 기둥이 앞에 오도록 정렬
    result.sort(key=lambda x: x[2])
    result.sort(key=itemgetter(0, 1))  # x, y 좌표 순으로 오름차순 정렬

    # 결과 리턴
    return result


if __name__ == "__main__":
    print(solution([[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))