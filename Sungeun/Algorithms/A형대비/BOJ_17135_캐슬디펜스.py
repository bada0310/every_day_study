# 17135_캐슬디펜스 
# 시물레이션 
N, M, D = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]
# |r1-r2| + |c1-c2|
archor = []
res = []
def comb(depth, start):
    if depth == 3: # 궁수 3명을 뽑을 조합
        archor.append(res[:])
        return
    for i in range(start,N):
        res.append(i)
        comb(depth+1,i+1)
        res.pop()
comb(0,0)

def kill_mon(case, curr_grid):
    target = set()
    for a_c in case:
        a_r = N 
        candidate = []
        for x in range(N):
            for y in range(M):
                if curr_grid[x][y] == 1:
                    dist = (abs(a_r -x)+abs(a_c -y))
                    if dist <= D:
                        candidate.append((dist,x,y)) # 죽일수 있는 후보군에 넣기 
    if candidate:
        candidate.sort()
        d, final_x,final_y = candidate[0] # 후보군 중 가장 왼쪽만 최종으로 죽임
        target.add((final_x,final_y))
    cnt =len(target)
    for tx, ty in target:
        curr_grid[tx][ty] = 0
    return cnt

ans = 0
for case in archor:
    curr_grid = [line[:] for line in grid]
    kill_total = 0
    for _ in range(N):
        kill_total += kill_mon(case, curr_grid)
        
        arr = [0]*M
        curr_grid.insert(0,arr)
        curr_grid.pop()
        ans = max(ans,kill_total)
print(ans)
