n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
winds = [tuple(map(int, input().split())) for _ in range(q)]

for r1, c1, r2, c2 in winds:
    r1, c1, r2, c2 = r1 - 1, c1-1, r2-1, c2-1 # 좌표 보정 
    a = [row[c1:c2+1] for row in grid[r1:r2+1]]
    M, N = len(a), len(a[0]) # N, M = c2-c1+1, r2 -r1+1
    # 부분 상자 가져오기 
    coords = []
    for c in range(N): coords.append((0, c))          # 상단 행
    for r in range(1, M): coords.append((r, N-1))     # 우측 열
    for c in range(N-2, -1, -1): coords.append((M-1, c)) # 하단 행
    for r in range(M-2, 0, -1): coords.append((r, 0))    # 좌측 열
    # 회전 연산 
    values = [a[r][c] for r, c in coords]
    values = [values[-1]] + values[:-1]
    for (r, c), val in zip(coords, values):
        grid[r1 + r][c1 + c] = val
    # 반영
    a = [row[c1:c2+1] for row in grid[r1:r2+1]]
    new_a = [row[:] for row in a]
    # 평균 계산 
    for r in range(M): 
        for c in range(N):
            curr_r, curr_c = r1 + r, c1 + c
            s = grid[curr_r][curr_c] 
            count = 1
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    s += grid[nr][nc]
                    count += 1
            new_a[r][c] = s // count
    for r in range(M):
        grid[r1 + r][c1 : c2 + 1] = new_a[r]  
        
for row in grid:
    print(*row) 
            
    # for r in range(M):
    #     grid[r1 + r][c1 : c2 + 1] = a[r]
    

        
    