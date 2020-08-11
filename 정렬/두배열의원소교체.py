if __name__ == "__main__":

    # 입력
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # A 오름차순 정렬
    A.sort()

    # B 내림차순 정렬
    B.sort(reverse=True)

    # A와 B 앞에서부터 K만큼 교체(바꾸는 수가 작은 경우 종료)
    for i in range(K):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
        else:
            break

    # 합 출력
    print(sum(A))