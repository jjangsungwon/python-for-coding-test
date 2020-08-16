if __name__ == "__main__":
    S = input()

    # 1로 만들기
    one_count = 0
    one_flag = True
    for i in range(len(S)):
        if int(S[i]) == 0 and one_flag:  # 이전 값이 1이고 현재 값이 0인 경우
            one_flag = False  # 현재 값이 0을 나타내고 있다.
        else:
            if not one_flag:  # 현재 값이 0인 경우
                if int(S[i]) == 1:
                    one_count += 1
                    one_flag = True
                else:
                    continue
    if not one_flag:
        one_count += 1
    # 0으로 만들기
    zero_count = 0
    zero_flag = True
    for i in range(len(S)):
        if int(S[i]) == 1 and zero_flag:  # 이전 값이 0이고 현재 값이 1인 경우
            zero_flag = False  # 현재 값이 1을 나타내고 있다.
        else:
            if not zero_flag:  # 현재 값이 1인 경우
                if int(S[i]) == 0:
                    zero_count += 1
                    zero_flag = True
                else:
                    continue
    if not zero_flag:
        zero_count += 1
    # 더 작은 값을 출력
    print(min(one_count, zero_count))