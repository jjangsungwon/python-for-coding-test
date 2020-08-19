def correct_bracket(arr):  # 올바른 괄호 문자열 판단
    stack = []
    for i in range(len(arr)):
        if arr[i] == "(":
            stack.append("(")
        else:
            if len(stack) == 0:  # 괄호의 짝이 맞지 않는 경우
                return False
            else:
                stack.pop()
    if len(stack) != 0:  # 왼쪽 괄호와 오른쪽 괄호 개수가 일치하지 않는 경우
        return False
    else:
        return True



def solution(p):
    # Case 1 : 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if len(p) == 0:
        return ""
    else:
        # Case 2 : 문자열을 두 균형잡힌 괄호 문자열로 분리
        left_bracket, right_bracket = 0, 0
        for i in range(len(p)):
            if p[i] == "(":
                left_bracket += 1  # 왼쪽 괄호 개수 증가
            else:
                right_bracket += 1  # 오른쪽 괄호 개수 증가
            if left_bracket == right_bracket:  # u를 찾은 상황
                u = p[:i + 1]
                v = p[i + 1:]
                break
        if correct_bracket(u):  # u가 올바른 괄호 문자열인 경우
            return u + solution(v)
        else:  # u가 올바른 괄호 문자열이 아닌 경우
            temp = "("
            temp += solution(v)
            temp += ")"
            u = u[1:-1]  # 첫 번째, 마지막 문자 제거
            u = list(u)
            for i in range(len(u)):  # 문자열 괄호 방향 뒤집기
                if u[i] == "(":
                    u[i] = ")"
                else:
                    u[i] = "("
            temp += "".join(map(str, u))

            return temp


if __name__ == "__main__":
    print(solution("()))((()"))
