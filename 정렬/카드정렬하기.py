import heapq


if __name__ == "__main__":
    n = int(input())  # 카드의 수
    q = []

    # 우선순위 큐에 카드 입력
    for _ in range(n):
        heapq.heappush(q, int(input()))

    answer = 0
    while len(q) != 1:
        first = heapq.heappop(q)
        second = heapq.heappop(q)
        answer += first + second
        heapq.heappush(q, first + second)

    print(answer)