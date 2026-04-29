N, M, D = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

def get_dist(r1,c1, r2, c2):
    return abs(r1-r2) + abs(c1 -c2)

# 궁수 3명 배치 위치 
# 직접적으로 arr 를 만들지말고 들어갈 열만 선택하는 조합을 만들어라 
archor = []
choice = []
def comb(start, count):
    if count == 3:
        archor.append(choice[:]) # shallow copy 
        return
    for i in range(start,M):
        choice.append(i)
        comb(i+1,count+1)
        choice.pop()
comb(0,0)
# 궁수들의 위치


# 거리 D 까지 몬스터 죽이기  + 얼만지 세기 
def kill_mon(case, curr_grid): # bfs?  # 왼쪽부터 탐색하도록
    target = set()
    for a_c in case:
        a_r = N 
        candidate = []
        for x in range(N):
            for y in range(M):
                if curr_grid[x][y] == 1:
                    dist = (abs(a_r - x)+ abs(a_c - y))
                    if dist <= D: # 범위 내에 존재하면 죽여!
                        candidate.append((dist,y,x))
                        # 거리가 가장 짧고/ 왼쪽에 있는것 
        if candidate:
            candidate.sort()
            d, final_y, final_x = candidate[0]
            target.add((final_x, final_y))
    cnt = len(target)
    for tx, ty in target:
        curr_grid[tx][ty] = 0
    return cnt



# 최종 함수 
answer = 0
# 복사하는 부분
for case in archor:
    curr_grid = [line[:] for line in grid]
    kill_total = 0

    for _ in range(N):
        kill_total += kill_mon(case, curr_grid)

        arr= [0]*M
        curr_grid.insert(0, arr)
        curr_grid.pop()
    answer = max(answer, kill_total)
print(answer)