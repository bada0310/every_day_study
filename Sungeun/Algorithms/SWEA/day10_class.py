# 가장 높은 봉우리가 여러개인 경우에 모두 깎을 수 없습니다. 
# 라는 조건을 고려해야함 
def dfs(r, c, h, dig, length):
    global max_dist
    if length > max_dist:
        max_dist = length
        
    visited[r][c] = True
    for dx, dy in dir:
        nx, ny = r + dx, c + dy
        if 0<= nx < N and 0<= ny < N and not visited[nx][ny]:
            if grid[nx][ny] < h:
                dfs(nx, ny, grid[nx][ny], dig,length+1)
                
            elif dig:
                if grid[nx][ny]-K < h:
                    temp = grid[nx][ny]
                    target_h = h-1
                if target_h >= 1:
                    grid[nx][ny] = target_h
                    dfs(nx,ny, target_h, False, length + 1)
                    grid[nx][ny] = temp
    visited[r][c] =False
    
N, K = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
dir = [(0,1),(1,0),(-1,0),(0,-1)]

max_dist = 0
max_h = 0     
# max_height
for row in grid:
    max_h = max(max_h, max(row))
# find max_height_pos  
starts = []
for r in range(N):
    for c in range(N):
        if grid[r][c] == max_h:
            starts.append((r,c))

for sr, sc in starts:
    dfs(sr,sc, max_h, True, 1)
print(max_dist)
                    

# 강사님 풀이 
from collections import deque

N = int(input())
lst = list(map(int, input().split()))

lst1 = deque()
lst2 = deque()

for i in range(N):
    if i < N // 2:
        lst1.append(lst[i])
    else:
        lst2.append(lst[i])

card_lst = []

while len(lst1) != 0 and len(lst2) != 0:
    if (lst1[0] + lst2[0])%2 == 1:
        card_lst.append(lst1[0])
        lst1.popleft()
    else:
        card_lst.append(lst2[0])
        lst2.popleft()

if len(lst) > 0:
    for i in range(len(lst1)):
        card_lst.append(lst1[i])
if len(lst) > 0:
    for j in range(len(lst2)):
        card_lst.append(lst2[j])

print(*card_lst)
# IM 과제 
N, K = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

def has_reef(y, x, K):
    # 1중 for문으로 해결할 방법을 찾기.
    # for i in range(y, y + K):
    #     for j in range(x, x + K):
    #         if (i == y or i == y + K - 1 or j == x or j == x + K - 1) and grid[i][j] == -1:
    #             return True
    return False


def count_fish(y, x, K):
    cnt = 0
    # 1중 for문으로 해결할 방법을 찾기.
    # for i in range(y, y + K):
    #     for j in range(x, x + K):
    #         if (i == y or i == y + K - 1 or j == x or j == x + K - 1):
    #             cnt += grid[i][j]
    return cnt

res = 0

for y in range(N - K + 1):
    for x in range(N - K + 1):
        if has_reef(y, x, K):
            continue

        res = max(res, count_fish(y, x, K))

print(res)

# A형 문제 풀이 
dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]

def in_range(y, x):
    return 0 <= y < N and 0 <= x < N

def get_movable(y, x, remains, moved_cnt, grid, visited):
    directions = []

    for i in range(4):
        ny = y + dys[i]
        nx = x + dxs[i]

        if not in_range(ny, nx):
            continue

        current_height = grid[y][x]
        next_height = grid[ny][nx]

        # 이미 방문한 방향인 경우
        if visited[ny][nx]:
            continue

        # 현재 가장 낮은 위치(1)에 있는 경우
        if current_height == 1:
            continue

        # 가장 높은 봉우리
        if next_height == highest:
            continue

        # 현재 remains로 이동이 어려운 경우
        cut = current_height - next_height + 1
        if remains < cut:
            continue

        directions.append(i)
    
    return directions

def move(y, x, remains, moved_cnt, grid, visited):
    directions = get_movable(y, x, remains, moved_cnt, grid, visited)
    return_value = moved_cnt

    if len(directions) == 0:
        return moved_cnt

    for i in directions:
        ny = y + dys[i]
        nx = x + dxs[i]

        current_height = grid[y][x]
        next_height = grid[ny][nx]

        visited[ny][nx] = True

        if current_height > next_height:
            return_value = max(return_value, move(ny, nx, remains, moved_cnt + 1, grid, visited))
        else:
            cut = current_height - next_height + 1
            grid[ny][nx] = current_height - 1
            return_value = max(return_value, move(ny, nx, remains - cut, moved_cnt + 1, grid, visited))
            grid[ny][nx] = next_height

        visited[ny][nx] = False

    return return_value



