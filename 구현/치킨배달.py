from itertools import combinations
import sys


if __name__ == "__main__":

    # 입력
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]

    # 치킨집 정보 저장
    chicken = []
    for i in range(N):
        for j in range(N):
            if array[i][j] == 2:
                chicken.append((i, j))
                array[i][j] = 0  # 치킨집 없다고 가정

    # 치킨집에서 M개를 선택하고 치킨 거리를 계산한다.
    combinations_list = list(combinations(chicken, M))
    distance = sys.maxsize  # 치킨 거리 초기화
    for k in range(len(combinations_list)):
        temp = 0  # 해당 조합의 치킨집만 있을때 치킨 거리
        # 치킨 거리 계산
        for i in range(N):
            for j in range(N):
                if array[i][j] == 1:  # 집
                    temp_value = sys.maxsize
                    for r, c in combinations_list[k]:
                        temp_value = min(temp_value, abs(i - r) + abs(j - c))  # 해당 집에서 가장 가까운 치킨집 거리 계산
                    temp += temp_value
        distance = min(distance, temp)

    # 출력
    print(distance)