# dfs 갈수 있는 모든 공간을 탐색하는 문제
# + 만약 청소되지 않은 칸이 없는경우 뒤로 한칸 이동한다 
# 그리고 더이상 이동할수 없으면 break 
# 본인이  visit 한 길 == 청소한 길 

def is_range(r,c):
    return 0<= r < N and 0<= c < M

def clean(r,c,d):
    global cnt
    if not visited[r][c]:
        visited[r][c] = True 
        cnt += 1 # first block 
    
    dr = [-1,0,1,0]
    dc = [0,1,0,-1] # 북동 남서 
    
    for _ in range(4):
        d = (d+3) %4 
        nr, nc = r + dr[d], c + dc[d]
        if is_range(nr,nc):
            if not visited[nr][nc] and grid[nr][nc] == 0:
                clean(nr,nc,d)
                return
    back_r ,back_c = r - dr[d], c - dc[d]
    if is_range(back_r, back_c) and grid[back_r][back_c] != 1:
        clean(back_r,back_c,d) #뒤로 후진
    else:
        return

N, M = map(int,input().split())
r,c, d = map(int,input().split()) # curr_x, curr_y , dir 
grid = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
cnt  = 0

clean(r,c,d)
print(cnt)