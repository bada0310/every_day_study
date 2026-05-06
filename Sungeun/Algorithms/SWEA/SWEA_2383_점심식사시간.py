# 계단 입구 3,5 3,5 는 길이 
# 모두가 계단을 다 내려갔을 떄 걸리는 시간 
# - 이미 계단을 3명이 내려가고 있는 경우, 
# 그 중 한 명이 계단을 완전히 내려갈 때까지 계단 입구에서 대기해야 한다.
# 이미 3명이 있을 경우 어떻게 대처해야하는가? 돌아가는것이 더 빠른가 대기하는 것이 더 빠른가 
from collections import deque

def dist(ex,ey,r,c):
    return abs(r-ex)+abs(c-ey)+1 # 도착하는 시간 

def time(r,c,arr): # end_point 의 좌표랑 team1
    arrive = []
    q = deque([0]) # 3칸을 
    for i in range(len(arr)):
        cr, cc = arr[i]
        arrive.append((dist(r,c,cr,cc) + 1))
    stair_length = grid[r][c]
    arrive.sort()
    for k in range(len(arrive)):

        if len(q) >= 3:
            start_time = max(arrive[k], q.popleft())
            q.append(start_time + stair_length)
        else:
            q.append(arrive[k]+ stair_length)
   
    return q[-1] if q else 0

def comb(depth):
    global min_time 
    if depth == L:
        # print(team1)
        time1 = time(end_point[0][0], end_point[0][1],team1)
        time2 = time(end_point[1][0], end_point[1][1],team2)
        end_time = max(time1,time2)
        
        min_time = min(min_time,end_time)
        return
    # print(depth)
    team1.append(human[depth])
    # print(team1)

    comb(depth+1)
    team1.pop()
    

    team2.append(human[depth])
    comb(depth+1)
    # print(team1)
    
    team2.pop()

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    end_point = [] # 계단의 좌표 및 길이 저장 lst len(end_point)=2
    human= []
     # 사람의 수 
    for i in range(N):
        for j in range(N):
            if grid[i][j] not in [0,1]:# 0과 1외의다른 수들 = 계단 
                end_point.append((i,j,grid[i][j])) # x ,y ,길이
            elif grid[i][j] == 1:
                human.append((i,j))
                
    L = len(human)
    min_time = int(1e9)
    team1 = [] # only 1번
    team2 = []
    comb(0)

    print(f'#{tc}',min_time-1)

