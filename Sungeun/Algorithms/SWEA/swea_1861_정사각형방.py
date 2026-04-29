# from collections import deque
# dir = [(0,1),(1,0),(-1,0),(0,-1)]
# def bfs(r,c):
#     q = deque([(r,c)])
#     curr_dist = 0
#     curr_x, curr_y = r, c
#     while True:
#         found = False # flag
#         for dx, dy in dir:
#             nx, ny = curr_x + dx, curr_y +dy
#             if 0<= nx < N and 0<= ny < N :
#                 if grid[nx][ny] == grid[curr_x][curr_y] +1:
#                     curr_x, curr_y = nx, ny
#                     curr_dist += 1
#                     found = True
#                     break
#         if not found:
#             break
#     return curr_dist

# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     grid = [list(map(int,input().split())) for _ in range(N)]
#     ans_start = float('inf')
#     ans_dist = 0
#     for i in range(N):
#         for j in range(N):
#             dist = bfs(i,j)
#             if dist > ans_dist:
#                 ans_dist = dist
#                 ans_start =grid[i][j]
#             elif dist == ans_dist:
#                 if grid[i][j] < ans_start:
#                     ans_start = grid[i][j]
#     print(f'#{tc}',ans_start ,ans_dist)

# dfs + memoization
from collections import deque
dir = [(0,1),(1,0),(-1,0),(0,-1)]
def is_range(r,c):
    return 0<= r< N and 0<= c < N
def dfs(r, c):
    if memo[r][c] != 0:
        return memo[r][c]
    
    memo[r][c] = 1
    
    for dx, dy in dir:
        nx, ny = r + dx ,c + dy
        if is_range(nx,ny) and grid[nx][ny] == grid[r][c] + 1:
            memo[r][c] = dfs(nx,ny)+1
            break
    return memo[r][c]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    memo = [[0]*N for _ in range(N)]
    ans_start = 0
    ans_dist = 0
    
    for i in range(N):
        for j in range(N):
            dist = dfs(i,j)
            
            if dist > ans_dist:
                ans_dist = dist
                ans_start = grid[i][j]
            elif dist == ans_dist:
                if grid[i][j] < ans_start:
                    ans_start = grid[i][j]
    print(f'#{tc}',ans_start,ans_dist)
        