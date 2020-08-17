def solution(s):
    # 입력받은 문자열의 길이 파악
    length = len(s)
    answer = length  # 길이 초기값

    # 단위 1부터 length - 1까지 완전 탐색
    for i in range(1, length):
        word = s[:i]  # 단어 초기값
        count = 1  # 개수 초기값
        result = []  # 현재 단위로 잘랐을 때 최종 문자열 저장
        for j in range(i, length, i):
            if word == s[j:j+i]:  # 동일 단어
                count += 1  # 개수 증가
            else:
                if count == 1:
                    result.append(word)  # 단어의 개수가 1개이면 단어만 삽입
                else:  # 갯수가 2개 이상인 경우
                    result.append(str(count) + word)  # 숫자와 단어 함께 삽입
                word = s[j:j+i]  # word 변경
                count = 1  # count 1로 초기화
            if j == length - i:  # 더 이상 탐색할 수 없을 때(word에 담긴것을 삽입)
                if count == 1:
                    result.append(word)
                else:
                    result.append(str(count) + word)
            elif j + i >= length:  # 더 이상 탐색를 자를 수 없을 때(뒤에 단어를 그대로 삽입)
                result.append(s[j:])

        # 길이 업데이트
        answer = min(answer, len("".join(map(str, result))))
    return answer


if __name__ == "__main__":
    print(solution("aabbaccc"))
