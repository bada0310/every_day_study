# dfs - > back trakc 
# min spanning tree (kruskal, prim, priority que)
from collections import deque

N, M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
visited =[[False]*M for _ in range(N)]
ans = float('inf') # 최솟값구하기 위한 

# def bridge(sr,sc,dx,dy,length, val):
#     for i in range(1, length+1):
#         grid[sr+dx*i][sc + dy * i] = val

# in_range
def is_range(r,c):
    return 0<= r < N and 0<= c < M  # True or False 
# count component 
def bfs_component(r,c,num):
    q = deque([(r,c)])
    visited[r][c] = True
    grid[r][c] = num

    while q:
        curr_x, curr_y = q.popleft()
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        for dx, dy in dir: 
            nx, ny = curr_x + dx ,curr_y +  dy
            if 0<= nx < N and 0<= ny < M:
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    grid[nx][ny] = num
                    q.append((nx,ny))   

def search():
    num = 1
    for i in range(N):
        for j in range(M): 
            if grid[i][j] == 1 and not visited[i][j]:
                bfs_component(i,j,num)
                num += 1    
    return num -1 

total_island = search() #총 섬의 갯수 

def dfs(curr_dist,connected_count, visited_island): # r, c,curr_ dist , connected_count
    global ans
    
    if connected_count == total_island:
        ans = min(ans,curr_dist)
        return
    
    dir = [(0,1),(1,0),(-1,0),(0,-1)]
    
    for i in range(N):
        for j in range(M): # 세상에나 마상에나 M 인데
            curr_island = grid[i][j] # start 
            if grid[i][j] == curr_island and visited_island[grid[i][j]]:
        
                for dx, dy in dir:
                    nx, ny = i + dx ,j +  dy
                    dist = 0
                    
                    while is_range(nx,ny) and grid[nx][ny] == 0: # bridge
                        nx += dx
                        ny += dy
                        dist += 1
                        
                        if is_range(nx,ny) and grid[nx][ny] > 0:
                            next_island = grid[nx][ny]
                            
                            if dist >= 2 and not visited_island[next_island]:
                                visited_island[next_island] = True
                                dfs(curr_dist + dist, connected_count + 1, visited_island)
                                visited_island[next_island] = False

found = False # flag
for i in range(N):
    for j in range(M):
        if grid[i][j] >0:
            visited_island = [False]*(total_island+1)
            start_island = grid[i][j]
            visited_island[start_island] = True
            dfs(0,1,visited_island)
            
            found = True
            break
        
    if found: break
print(ans if ans != float('inf') else -1)
