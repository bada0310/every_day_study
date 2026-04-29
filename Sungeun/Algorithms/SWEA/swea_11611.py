T = int(input())

def combination(grid,N):
    min_val = 1000000
    used_col = [False]*N
    def generate(row, curr_sum):
        nonlocal min_val
        if curr_sum >= min_val: # 연산과정이 많기 때문에 쓸데없는 값은 비교하지 않도록 추가 해준다 
            return
        if row == N:
            if curr_sum < min_val:
                min_val = curr_sum
            return
        
        for j in range(N):
            if not used_col[j]:
                used_col[j] =True
                generate(row+1, curr_sum + grid[row][j])# 재귀 
                # 백트래킹 
                used_col[j] = False
    generate(0,0)
    return min_val

for t in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    res = combination(grid,N)
    print(f"#{t}",res)