# 최고의 33위치

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
directions =[ (-1,-1), (-1, 0),(-1,1), (0,1),(0,-1),(1,-1),(1,0),(1,1)]
max_val = 0
for r in range(n):
    for c in range(n):
        s = grid[r][c]
        
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc 
            if 0<= nr < n and 0<= nc < n:
                s += grid[nr][nc]
        if max_val < s:
            max_val = s
print(max_val)