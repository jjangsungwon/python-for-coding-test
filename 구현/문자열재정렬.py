if __name__ == "__main__":

    # 입력
    string = input()

    # 입력받은 문자열을 탐색하면서 따로 구현한 문자열 배열에 문자를 삽입하고, 숫자는 누적해서 더한다.
    sort_string = []
    total = 0
    for i in string:
        if i.isalpha():
            sort_string.append(i)
        else:
            total += int(i)

    result = sorted(sort_string)
    if total != 0:
        result.append(total)
    print("".join(map(str, result)))