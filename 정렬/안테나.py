import sys

if __name__ == "__main__":
    n = int(input())  # 집의 수
    home = list(map(int, input().split()))

    # 오름차순 정렬
    home.sort()

    location = -1
    min_distance = sys.maxsize  # 큰 수로 초기화
    post_distance = sum(home[1:])  # 모든 집의 거리 합
    pre_distance = 0  # 현재 위치 이전 집들의 합
    for i in range(n):  # 각 집에 안테나를 설치해보고 거리값 비교
        if pre_distance == 0:
            distance = post_distance - (n - (i + 1)) * home[i]
        else:
            distance = (home[i] * i - pre_distance) + (post_distance - home[i] * (n - i - 1))

        pre_distance += home[i]
        if i != n - 1:
            post_distance -= home[i + 1]

        if distance < min_distance:
            min_distance = distance
            location = home[i]

    # 출력
    print(location)
