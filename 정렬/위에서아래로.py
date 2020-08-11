if __name__ == "__main__":
    N = int(input())  # ㅅ열에 속해 있는 수의 개수
    data = [int(input()) for _ in range(N)]

    # 내림차순 정렬
    data.sort(reverse=True)

    # 출력
    print(" ".join(map(str, data)))