# 최단 거리 >> bfs
# 시작 지점-> 끝 지점 주어짐 
# grid 는 회전 가능/뒤집기는 안됌
# grid 를 쌓는 순서도 자유로움

from collections import deque

dx = [0,0,0,0,1,-1]
dy = [-1,1,0,0,0,0]
dz = [0,0,-1,1,0,0] # 이거 못만들어서 물어봄...;;;
def is_range(z,y,x):
    return 0<= z <5 and 0<= y < 5 and 0<= x <5 

def rotate_90(board): # 회전
    return [list(row) for row in zip(*board[::-1])]

def find_maze(cube):# bfs

    q = deque([(0,0,0,0)]) # z, y, x,
    visited = [[[False]*5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True
    
    while q:
        z, y, x, dist = q.popleft()

        if z == 4 and y == 4 and x == 4:
            return dist
        for i in range(6):
            nz, ny, nx = z +dz[i], y + dy[i], x + dx[i]
            if is_range(nz,ny,nx):
                if cube[nz][ny][nx] == 1 and not visited[nz][ny][nx]:
                    visited[nz][ny][nx] = True
                    q.append((nz,ny,nx, dist+1))
    return -1

def perm(depth):
    global ans 
    if depth == 5:
        if cube[0][0][0] == 1 and cube[4][4][4] == 1:
            res = find_maze(cube) # 여기서 적용
            if res !=  -1:
                ans = min(ans, res)
        return

    for i in range(5):
        if not used[i]:
            used[i] = True

            for rot in range(4):
                cube[depth] = rotate_grid[i][rot]
                perm(depth + 1)
            used[i] = False 

cube = [[list(map(int,input().split())) for _ in range(5)] for _ in range(5)]

rotate_grid = [[[] for _ in range(4)] for _ in range(5)]
for i in range(5):
    rotate_grid[i][0] = cube[i]
    for j in range(1,4): #0번은 채웠으니 1,~3까지만 채우면 된다. 
        rotate_grid[i][j] = rotate_90(rotate_grid[i][j-1])
ans = float('inf')

used = [False]*5
cube = [None]*5

perm(0)
print(ans if ans !=float('inf') else -1)

# try2 (런타임 에러 뜸)
from collections import deque

dx = [0,0,0,0,1,-1]
dy = [-1,1,0,0,0,0]
dz = [0,0,-1,1,0,0] # 이거 못만들어서 물어봄...;;;
def is_range(z,y,x):
    return 0<= z <5 and 0<= y < 5 and 0<= x <5 

def rotate_90(board): # 회전
    return [list(row) for row in zip(*board[::-1])]

def find_maze(cube):# bfs

    q = deque([(0,0,0,0)]) # z, y, x,
    visited = [[[False]*5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True
    
    while q:
        z, y, x, dist = q.popleft()

        if z == 4 and y == 4 and x == 4:
            return dist
        for i in range(6):
            nz, ny, nx = z +dz[i], y + dy[i], x + dx[i]
            if is_range(nz,ny,nx):
                if cube[nz][ny][nx] == 1 and not visited[nz][ny][nx]:
                    visited[nz][ny][nx] = True
                    q.append((nz,ny,nx, dist+1))
    return -1

def perm(depth):
    global ans

    if ans == 12: # (0,0,0) - > (4,4,4) = 4 + 4 + 4 = 12 이기 때문에 (prunning 가능)
        return


    if depth == 5:
        if cube[0][0][0] == 1 and cube[4][4][4] == 1:
            res = find_maze(cube) # 여기서 적용
            if res !=  -1:
                ans = min(ans, res)
        return

    for i in range(5):
        if not used[i]:
            used[i] = True

            for rot in range(4):
                cube[depth] = rotate_grid[i][rot]
                perm(depth + 1)
            used[i] = False 

cube = [[list(map(int,input().split())) for _ in range(5)] for _ in range(5)]

rotate_grid = [[[] for _ in range(4)] for _ in range(5)]
for i in range(5):
    rotate_grid[i][0] = cube[i]
    for j in range(1,4): #0번은 채웠으니 1,~3까지만 채우면 된다. 
        rotate_grid[i][j] = rotate_90(rotate_grid[i][j-1])
ans = float('inf')

used = [False]*5
cube = [None]*5

perm(0)
print(ans if ans !=float('inf') else -1)
