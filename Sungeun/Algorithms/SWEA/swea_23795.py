import sys
sys.stdin = open("sample_in.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for x in range(N):
        for y in range(N):

            if grid[x][y] == 2:
                for i in range(4):
                    nx, ny = x + dx[i] , y + dy[i]
                    while 0 <= nx < N and 0 <= ny < N:
                        if grid[nx][ny] == 1 or grid[nx][ny] == 2:
                            break
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 3

                        nx += dx[i]
                        ny += dy[i]
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                count += 1
    print(f"#{t} {count}")