import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return - 1

    # 우선순위 큐 (시간, 번호)
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0  # 음식을 먹기 위해 사용한 시간
    pre_value = 0  # 이전까지의 시간
    length = len(food_times)  # 길이

    # 총 시간 + (현재 시간 - 이전까지의 시간) * 길이와 K의 값 비교
    while sum_value + (q[0][0] - pre_value) * length <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - pre_value) * length
        pre_value = now
        length -= 1

    # 해당 인덱스 값 찾아서 반환
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]


if __name__ == "__main__":
    print(solution([3, 1, 2], 5))
