if __name__ == "__main__":

    # 입력
    N = int(input())

    # 초기화
    h, m, s = 0, 0, 0  # 시, 분, 초
    count = 0

    # 목표 시간까지 반복
    while True:
        if h == N and m == 59 and s == 59:
            break
        s += 1
        if s == 60:
            s = 0
            m += 1
            if m == 60:
                m = 0
                h += 1

        temp = list(str(h) + str(m) + str(s))
        if '3' in temp:
            count += 1

    print(count)