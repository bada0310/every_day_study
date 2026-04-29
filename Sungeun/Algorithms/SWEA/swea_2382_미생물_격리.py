dx =[0,-1,1,0,0]
dy = [0,0,0,-1,1]

rev_d = {1:2, 2:1, 3:4,4:3}
def move_micro(arr, N):
    next_pos = {}

    for x, y, num, d in arr:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx == 0 or nx == N-1 or ny == 0 or ny== N-1:
            num = num//2
            d =rev_d[d]

        if num > 0:
            if (nx,ny) not in next_pos:
                next_pos[(nx,ny)] = []
            next_pos[(nx, ny)].append((num, d))
    #갱신
    new_micro = [] 
    for (x,y), groups in next_pos.items():
        if len(groups) == 1:
            new_micro.append((x,y,groups[0][0], groups[0][1]))
        else:
            total_num = 0
            max_num = 0
            main_d = 0

            for n, d in groups:
                total_num += n
                if n > max_num:
                    max_num = n
                    main_d = d
            new_micro.append((x,y,total_num,main_d))
    return new_micro

T = int(input())

for t in range(1, T+1):
    N, M, K = map(int,input().split()) # N*N
    grid = [[0]*M for _ in range(N)]
    micro = []
    for _ in range(K):
        x, y, num, d = map(int, input().split())
        micro.append((x,y,num,d))
    for _ in range(M):
        micro = move_micro(micro,N)

    ans = 0
    for x, y, num, d in micro:
        ans += num
    print(f'#{t}',ans)