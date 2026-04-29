# 가로 세로 9칸 박스 
def is_valid(grid, r, c, num):
    if num in grid[r]: #가로 
        return False
    if num in [grid[i][c] for i in range(9)]: # 세로
        return False
    sr, sc = (r//3)*3 , (c//3)*3 # 이걸 생각을 못해서 잼민이 한테 물어봤음!! 
    for i in range(sr, sr+3):
        for j in range(sc, sc +3):
            if grid[i][j] == num:
                return False
    return True

def solve(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0: # 값이 0이라면
                for num in range(1,10):
                    if is_valid(grid, r, c, num):
                        grid[r][c] = num
                        if solve(grid): return True # 다음 빈칸 찾으려고 재귀 호출 
                        grid[r][c] = 0 # 백 트래킹 
                return False
    return True

grid = [list(map(int,input().split())) for _ in range(9)]

if solve(grid):
    for row in grid:
        print(*row)