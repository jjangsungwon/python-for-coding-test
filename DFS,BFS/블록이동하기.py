from collections import deque


def bfs(board):
    length = len(board)
    q = deque()
    q.append([(0, 0, 0, 1), 0, 0])  # 로봇 위치, 방향, 이동 횟수 정보 저장
    visited = set()  # 방문 정보 저장
    visited.add((0, 0, 0, 1))

    while q:
        location, direction, count = q.popleft()
        left = location[:2]
        right = location[2:]

        if left == (length - 1, length - 1) or right == (length - 1, length - 1):  # (N, N) 도달
            return count

        if direction == 0:  # 가로 방향
            # 상
            if left[0] - 1 >= 0 and right[0] - 1 >= 0 and board[left[0] - 1][left[1]] == 0 and board[right[0] - 1][right[1]] == 0 and (left[0] - 1, left[1], right[0] - 1, right[1]) not in visited:
                visited.add((left[0] - 1, left[1], right[0] - 1, right[1]))  # 방문 체크
                q.append([(left[0] - 1, left[1], right[0] - 1, right[1]), direction, count + 1])

                # 위쪽 방향으로 회전도 가능
                visited.add((left[0] - 1, left[1], left[0], left[1]))
                q.append([(left[0] - 1, left[1], left[0], left[1]), 1, count + 1])

                visited.add((right[0] - 1, right[1], right[0], right[1]))
                q.append([(right[0] - 1, right[1], right[0], right[1]), 1, count + 1])
            # 하
            if left[0] + 1 < length and right[0] + 1 < length and board[left[0] + 1][left[1]] == 0 and board[right[0] + 1][right[1]] == 0 and (left[0] + 1, left[1], right[0] + 1, right[1]) not in visited:
                visited.add((left[0] + 1, left[1], right[0] + 1, right[1]))  # 방문 체크
                q.append([(left[0] + 1, left[1], right[0] + 1, right[1]), direction, count + 1])

                # 아래쪽 방향으로 회전도 가능
                visited.add((left[0], left[1], left[0] + 1, left[1]))
                q.append([(left[0], left[1], left[0] + 1, left[1]), 1, count + 1])

                visited.add((right[0], right[1], right[0] + 1, right[1]))
                q.append([(right[0], right[1], right[0] + 1, right[1]), 1, count + 1])
            # 좌
            if left[1] - 1 >= 0 and board[left[0]][left[1] - 1] == 0 and (left[0], left[1] - 1, left[0], left[1]) not in visited:
                visited.add((left[0], left[1] - 1, left[0], left[1]))  # 방문 체크
                q.append([(left[0], left[1] - 1, left[0], left[1]), direction, count + 1])
            # 우
            if right[1] + 1 < length and board[right[0]][right[1] + 1] == 0 and (right[0], right[1], right[0], right[1] + 1) not in visited:
                visited.add((right[0], right[1], right[0], right[1] + 1))  # 방문 체크
                q.append([(right[0], right[1], right[0], right[1] + 1), direction, count + 1])
        else:  # 세로 방향
            # 상
            if left[0] - 1 >= 0 and board[left[0] - 1][left[1]] == 0 and (left[0] - 1, left[1], left[0] - 1, left[1]) not in visited:
                visited.add((left[0] - 1, left[1], left[0], left[1]))  # 방문 체크
                q.append([(left[0] - 1, left[1], left[0], left[1]), direction, count + 1])
            # 하
            if right[0] + 1 < length and board[right[0] + 1][right[1]] == 0 and (right[0], right[1], right[0] + 1, right[1]) not in visited:
                visited.add((right[0], right[1], right[0] + 1, right[1]))  # 방문 체크
                q.append([(right[0], right[1], right[0] + 1, right[1]), direction, count + 1])
            # 좌
            if left[1] - 1 >= 0 and board[left[0]][left[1] - 1] == 0 and board[right[0]][right[1] - 1] == 0 and (left[0], left[1] - 1, right[0], right[1] - 1) not in visited:
                visited.add((left[0], left[1] - 1, right[0], right[1] - 1))  # 방문 체크
                q.append([(left[0], left[1] - 1, right[0], right[1] - 1), direction, count + 1])

                # 왼쪽 방향으로 회전도 가능
                visited.add((left[0], left[1] - 1, left[0], left[1]))
                q.append([(left[0], left[1] - 1, left[0], left[1]), 0, count + 1])

                visited.add((right[0], right[1] - 1, right[0], right[1]))
                q.append([(right[0], right[1] - 1, right[0], right[1]), 0, count + 1])
            # 우
            if left[1] + 1 < length and right[1] + 1 < length and board[left[0]][left[1] + 1] == 0 and board[right[0]][right[1] + 1] == 0 and (left[0], left[1] + 1, right[0], right[1] + 1) not in visited:
                visited.add((left[0], left[1] + 1, right[0], right[1] + 1))  # 방문 체크
                q.append([(left[0], left[1] + 1, right[0], right[1] + 1), direction, count + 1])

                # 오른쪽 방향으로 회전도 가능
                visited.add((left[0], left[1], left[0], left[1] + 1))
                q.append([(left[0], left[1], left[0], left[1] + 1), 0, count + 1])

                visited.add((right[0], right[1], right[0], right[1] + 1))
                q.append([(right[0], right[1], right[0], right[1] + 1), 0, count + 1])


def solution(board):
    return bfs(board)


if __name__ == "__main__":
    print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
