# 17136_색종이붙이기 
# backtracking 
# 10 * 10 
grid = [list(map(int,input().split())) for _ in range(10)]
papers = [5]*5 # 1*1 2*2 3*3 4*4 5*5 각 5개 씩 
min_ans = float('inf')
# can_attach
def attach(r,c,size):
    if r + size > 10 or c + size:
        return
    for x in range(r, r+size):
        for y in range(c, c+size):
            if grid[x][y] == 0:
                return False
    return True

# color grid
def color_grid(r,c,size,state):
    for x in range(r, r+size):
        for y in range(c, c + size):
            grid[x][y] = state
 
def put(): # dfs
    global min_ans
    
    cur_page = 25 - sum(papers)
    if cur_page >= min_ans: # prunning
        return 
    for r in range(10):
        for c in range(10):
            if grid[r][c] == 1:
                for size in range(5,0,-1):
                    if attach(r,c,size) and papers[size-1]>0:
                        color_grid(r,c,size,0)
                        papers[size-1] -= 1

                        put()  # 재귀

                        color_grid(r,c,size,1)
                        papers[size-1] += 1
                    return
    min_ans = min(min_ans, cur_page)

put()
if min_ans == float('inf'):
    print(-1)
else:
    print(min_ans)
