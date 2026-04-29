# 이다솜 적어도 4명 S 적어도 3명 Y = 3
# 인접해 있어야 함 꼭
# (0,0) 부터 (4,4) 까지 시작점으로 해서 갈수 있는 
# 한칸씩 이동, 4방탐색,
# 한칸 이동하면 그거를 res 에 저장 하고 4방 탐색해서 갈수있는 방향을 선택
# visited[nx][ny] =True 확인 하고 res.append() 하고 
# q.append()
# 
# dist 를 7 로 두고
# dist == 7 이 되면 S의 갯수와 Y의 갯수를 센다 

grid = [list(input()) for _ in range(5)] # input() 
visited = [[False]*5 for _ in range(5)] # 방문 배열 
res = [] # 뽑은 좌표들 담을 리스트 각 case 에 대한 result 
# cnt = 0 # 칠공주 결성할 수 있는 경우의 수
result = set()

def is_range(r,c):
    return 0<= r < 5 and 0<= c <5 # 범위 내에 존재하는지 확인하는 함수 

def comb(depth, S_cnt, Y_cnt):
    global cnt
    if Y_cnt >= 4:
        return
    
    if depth == 7: # 길이 
        result.add(tuple(sorted(res)))
        return # 다음경우를 보기 
    
    for r, c in res:
        choose = [(r-1,c),(r,c-1),(r+1,c),(r,c+1)] # 지금 선택한 (r,c) 에서 볼수있는 4가지의 경우 
        for nx, ny in choose: # 각각 choose 에 있는 경우를 보기 
            if is_range(nx,ny) and not visited[nx][ny]: # 범위 내에 존재, 이미 방문한 내용인지 확인 
                res.append((nx,ny)) # case 에 넣기 
                visited[nx][ny] = True # 방문 확인 
                if grid[nx][ny] == 'S':
                    comb(depth+1,S_cnt+1,Y_cnt) # 재귀로 들어가기
                elif grid[nx][ny] == 'Y':
                    comb(depth+1,S_cnt, Y_cnt+1)

                visited[nx][ny] = False # 백트래킹 원상복구 하기 
                res.pop()# 백트래킹 원상복구 하기 

for i in range(5): # 이거를 모든 경우에 대해서 보기 위해 (0,0) ~ (4,4)까지
    for j in range(5):
        visited[i][j] = True
        res.append((i,j))

        if grid[i][j] == "S":
            comb(1,1,0)
        if grid[i][j] == 'Y':
            comb(1,0,1)
        res.pop()
        visited[i][j] = False

cnt = len(result)
print(cnt)


