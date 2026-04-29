import sys
input = sys.stdin.readline

R, C = map(int,input().split()) # 세로 R ,가로 C
grid = [list(input().strip()) for _ in range(R)]
# 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 
# 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
check_lst = set([grid[0][0]])
max_count = 0 # 말이 최대한 몇 칸을 지날 수 있는지
# dfs  써야함 
def dfs(r, c, count):
    global max_count
    max_count = max(max_count, count)
    
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        
        if 0<= nr < R and 0<= nc <C:
            if grid[nr][nc] not in check_lst:
                check_lst.add(grid[nr][nc])
                dfs(nr, nc, count + 1) # 재귀 
                check_lst.remove(grid[nr][nc]) # 백트래킹 
    return max_count

dfs(0,0,1)
print(max_count)
