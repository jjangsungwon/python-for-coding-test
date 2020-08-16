if __name__ == "__main__":
    S = input()

    if len(S) == 1:  # 문자열 S의 길이가 1인 경우
        print(S)
    else:
        # 문자열의 제일 첫 글자로 초기화
        answer = int(S[0])

        # 더하기와 곱하기 중에 결과값이 높은 것을 계속적으로 선택한다.
        for i in range(1, len(S)):
            answer = max(answer + int(S[i]), answer * int(S[i]))

        # 출력
        print(answer)