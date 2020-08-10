move = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]  # 상, 우, 하, 좌 기준으로 2개씩 나열


if __name__ == "__main__":
    col, row = input().strip()

    row = int(row)
    col = int(ord(col)) - int(ord('a')) + 1
    count = 0

    for r, c in move:
        new_row, new_col = row + r, col + c
        if 1 <= new_row <= 8 and 1 <= new_col <= 8:
            count += 1

    print(count)
