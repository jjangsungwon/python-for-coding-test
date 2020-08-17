if __name__ == "__main__":

    # 입력
    N = input()

    # 점수의 길이 파악
    length = len(N)

    # 절반으로 나누기
    mid = length // 2
    left = N[:mid]
    right = N[mid:]

    # 왼쪽의 합과 오른쪽의 합 계산
    left_sum = 0
    right_sum = 0
    for i in left:
        left_sum += int(i)
    for i in right:
        right_sum += int(i)

    # 값 비교 및 출력
    if left_sum == right_sum:
        print("LUCKY")
    else:
        print("READY")