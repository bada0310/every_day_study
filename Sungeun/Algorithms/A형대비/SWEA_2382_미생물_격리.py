# 미생물 
# 상 하 좌 우  # dir = [(-1,0),(1,0),(0,-1),(0,1)]

dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]
rev_d = {
    1:2,
    2:1,
    3:4,
    4:3
}

def move(arr):
    next_pos = {}
    for x, y, num, dir in arr:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
            num = num//2 
            dir = rev_d[dir]
        if num > 0:
            if (nx,ny) not in next_pos:
                next_pos[(nx,ny)] =[]
            next_pos[(nx,ny)].append((num,dir))
                
    new_micro = []
    for (x,y),group in next_pos.items():
        if len(group) == 1:
            new_micro.append((x,y,group[0][0], group[0][1]))
        else:
            total_num = 0
            max_num = 0
            main_d = 0
            for num, dir in group:
                total_num += num
                if num > max_num:
                    max_num = num
                    main_d = dir
            new_micro.append((x,y,total_num,main_d))
    return new_micro

T = int(input())
for tc in range(1,T+1):
    N, M, K =map(int,input().split()) # N*N time = M 
    grid = [[0]*N for _ in range(N)]
    arr = []
    for _ in range(K):
        r, c, num, dir = map(int,input().split())
        arr.append((r,c,num,dir))
    for _ in range(M):
        arr = move(arr)
    ans = 0
    for x, y, num, dir in arr:
        ans += num
    print(f'#{tc}',ans)
