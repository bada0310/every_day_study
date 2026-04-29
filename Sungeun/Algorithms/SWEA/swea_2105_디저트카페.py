dir = [(1,1),(1,-1),(-1,-1),(-1,1)] # 4대각방향 

def is_range(r,c):
    return 0<= r < N and 0<= c < N

def path_comb(r, c, w, h):
    visited_num =set()
    move_counts = [w,h,w,h]
    cx, cy = r,c 
    for i in range(4):
        for _ in range(move_counts[i]):
            cx += dir[i][0]
            cy += dir[i][1]
            if not is_range(cx,cy):
                return -1
            
            if grid[cx][cy] in visited_num:
                return -1
            visited_num.add(grid[cx][cy])
    return len(visited_num)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    max_diver = -1 # 최대 가짓수 
    for i in range(N):
        for j in range(N):
            for w in range(1,N):
                for h in range(1,N):
                    if 2*(w+h)<= max_diver:
                        continue
                    result = path_comb(i,j,w,h)
                    
                    if result != -1:
                        max_diver = max(max_diver, result)
    print(f'#{tc}', max_diver)

# test2
dir = [(1,1), (1,-1), (-1,-1), (-1,1)] 

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    max_diver = -1 
    
    for i in range(N - 2): 
        for j in range(1, N - 1): 
            for w in range(1, N):
                for h in range(1, N):
                    if 2 * (w + h) <= max_diver:
                        continue
                    if i + w + h >= N or j + w >= N or j - h < 0:
                        continue

                    visited = [False] * 101
                    cx, cy = i, j
                    possible = True
                    move_counts = [w, h, w, h]
                    
                    for d in range(4):
                        if not possible: break 
                            
                        for _ in range(move_counts[d]):
                            cx += dir[d][0]
                            cy += dir[d][1]
                            
                            dessert = grid[cx][cy]

                            if visited[dessert]:
                                possible = False
                                break
                                
                            visited[dessert] = True

                    if possible:
                        max_diver = max(max_diver, 2 * (w + h))
                        
    print(f'#{tc} {max_diver}')