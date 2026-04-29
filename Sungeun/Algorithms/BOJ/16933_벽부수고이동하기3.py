from collections import deque
import sys
input = sys.stdin.readline

# def is_range(r,c):
#     return 0<= r < N and 0<= c < M 

def bfs(r,c):
    q = deque([(r, c, 0, 1)]) # x, y, broken, time
    visited[r][c][0] = 1 # 

    while q:
        curr_x, curr_y, broken, time = q.popleft()
        
        if curr_x == N-1 and curr_y == M-1:
            return time
        
        wait = False # flag
        
        for dx, dy in dir:
            nx, ny = curr_x + dx ,curr_y + dy
            
            if 0<= nx < N and 0<= ny < M:
                if grid[nx][ny] == '0' and visited[nx][ny][broken] == 0: # no walls (dontcare day night)
                    visited[nx][ny][broken] = 1
                    q.append((nx,ny,broken,time + 1))
                # 벽을 만났을때 만약 밤이면 하루를 더기다려 낮으로 바꾸고 
                # 벽을 만났을때 만약 낮이면 부수고 카운트 한다. 
                elif grid[nx][ny] == '1' and broken < K:
                    if time %2 ==0: # 밤이면 낮이 될때까지 기다린다
                        wait = True
                        
                    elif time %2 == 1 and visited[nx][ny][broken+1] == 0:
                        visited[nx][ny][broken+1] = 1
                        q.append((nx,ny,broken+1,time+1))
        if wait:
            q.append((curr_x,curr_y,broken,time + 1))
    return -1



N, M, K = map(int, input().split())
grid = [input().strip() for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]  # x, y, 벽 부순 횟수
# 홀수 day 짝숫 night 
dir = [(0,1),(1,0),(-1,0),(0,-1)]

print(bfs(0,0))
# runtime error