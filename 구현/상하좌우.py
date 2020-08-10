if __name__ == "__main__":
    N = int(input())
    move = list(input().split())

    # [1, 1] 시작
    location = [1, 1]

    for m in move:
        if m == "L":
            if location[1] - 1 >= 1:
                location[1] -= 1
        elif m == "R":
            if location[1] + 1 <= N:
                location[1] += 1
        elif m == "U":
            if location[0] - 1 >= 1:
                location[0] -= 1
        elif m == "D":
            if location[0] + 1 <= N:
                location[0] += 1

    print(location[0], location[1])