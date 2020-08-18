import sys
from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    # weak * 2 를 통해서 원형의 구조를 선형으로 바꾼다.
    for i in range(length):
        weak.append(weak[i] + n)

    answer = sys.maxsize
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1  # 투입한 친구의 수
            limit = friends[count - 1] + weak[start]  # 갈 수 있는 거리
            for index in range(start, start + length):
                if weak[index] > limit:  # 거리를 초과하는 경우
                    count += 1  # 친구 투입
                    if count > len(dist):  # 더 이상 투입 할 친구가 없는 경우
                        break
                    limit = weak[index] + friends[count - 1]  # 길이 증가

            # 최솟값 업데이트
            answer = min(answer, count)

    if answer <= len(dist):
        return answer
    else:
        return -1


if __name__ == "__main__":
    print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
