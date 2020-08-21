if __name__ == "__main__":
    n = int(input())  # 학생 수
    student = []
    for _ in range(n):
        name, kor, math, eng = input().split()
        student.append([name, int(kor), int(math), int(eng)])

    # 정렬 (lambda 함수를 이용하여 다중 조건 정렬)
    student = sorted(student, key=lambda x: (-x[1], x[2], -x[3], x[0]))

    # 출력
    for i in range(n):
        print(student[i][0])
