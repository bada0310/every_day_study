M, N, H = map(int,input().split())
# value = dimension[h][n][m]  # [Z축][Y축][X축] 순서
grid = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

from collections import deque
def bfs(start_node):
    max_days = 0
    q = deque(start_node)

    while q:
        curr_z, curr_y, curr_x, d = q.popleft()
        max_days = d

        dir = [(1, 0, 0),(-1, 0, 0),(0, 1, 0),(0, -1, 0), (0, 0, 1),(0, 0, -1)]
        for dz, dy, dx in dir:
            nz = curr_z + dz
            ny = curr_y + dy
            nx = curr_x + dx
            if 0<= nx < M and 0<= ny < N and 0<= nz < H:
                if grid[nz][ny][nx] == 0:
                    grid[nz][ny][nx] = 1
                    q.append((nz, ny, nx, d + 1))

    for h in range(H):
        for y in range(N):
            if 0 in grid[h][y]:
                return -1
    return max_days
tomato = []
for h in range(H):
    for y in range(N):
        for x in range(M):
            if grid[h][y][x] == 1:
                tomato.append((h, y, x, 0))
print(bfs(tomato))