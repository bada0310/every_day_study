# # N queen 과 비슷한 문제 
# # dfs + back track 
def dfs(row):
    global max_ans, total_sum
    if row == 11:
        max_ans = max(max_ans, total_sum)
        return
    for col in range(11):
        if not visited[col] and grid[row][col] >0:
            visited[col] = True
            total_sum += grid[row][col]
            dfs(row+1)
            total_sum -=grid[row][col]
            visited[col] = False
            
T = int(input())
for t in range(T):
    grid = [list(map(int,input().split())) for _ in range(11)]
    visited = [False]*11
    max_ans = 0
    total_sum = 0
    for i in range(11):
        for j in range(11):
            if grid[i][j] > 0:
                dfs(i)
    print(max_ans)


# test 2 
def dfs(row, curr_sum):
    global max_ans
    if row == 11:
        max_ans = max(max_ans, curr_sum)
        return
    
    for col in range(11):
        if not visited[col] and grid[row][col] > 0:
            visited[col] = True
            dfs(row+1, curr_sum+grid[row][col])
            visited[col] = False
            
T = int(input())
for t in range(T):
    grid = [list(map(int,input().split())) for _ in range(11)]
    visited = [False]*11
    max_ans = 0
    dfs(0,0)
    print(max_ans)
            

