# 풀이 구성
# 방문한 곳 다시 방문 가능
# 서로 다른 일곱 자리 수들의 개수
# 변수에 (r,c,sum_val)로 받아오기 
# visited 배열로 풀어보기 
# sum_val 을 누적하면서 문제를 풀어보기 
def is_range(r,c):
    return 0<= r < 4 and 0<= c < 4

def dfs(r,c,curr_str,cnt):
    if cnt == 7:
        results.add(curr_str)
        return
    
    for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx,ny = r + dx, c + dy
        if is_range(nx,ny):
            dfs(nx,ny,curr_str + str(grid[nx][ny]),cnt+1)
  
T= int(input())
for tc in range(1, T+1):
    grid = [list(map(int,input().split())) for _ in range(4)]
    results = set()
    case_cnt = 0
    for i in range(4):
        for j in range(4):
            dfs(i,j,str(grid[i][j]),1)

    print(f'#{tc}',len(results))
    
    