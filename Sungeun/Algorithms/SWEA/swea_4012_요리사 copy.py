# 인접 행렬 
# 스타트 앤 링크 

def pair(team):
    score = 0
    for i in range(N//2):
        for j in range(N//2):
            score += grid[team[i]][team[j]]
    return score

def comb(depth,start):
    global min_abs
    if depth == N//2:
        team_a = result
        team_b = [i for i in range(N) if i not in team_a]

        diff = abs(pair(team_a)- pair(team_b))
        if diff < min_abs:
            min_abs = diff
        return
    
    for i in range(start, N):
        result.append(i)
        comb(depth+1,i+1)
        result.pop()

T = int(input())
for t in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    min_abs = float('inf')
    result = [] # case by case

    V= [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            V[i][j] = grid[i][j] + grid[i][j]
    comb(0,1)
    print(f'#{t}',min_abs)

# def comb(depth,start):
#     if depth == 2: # (x,y)
#         choice.append(tuple(result))
#         return 
#     for i in range(start,N+1):
#         result.append(i)
#         comb(depth+1,i+1)
#         result.pop()
# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     grid = [list(map(int,input().split())) for _ in range(N)]
#     min_abs = float('inf')
#     result = [] # case by case
#     choice = [] # total case 
#     arr = [] # grid val list
#     comb(0,1)  
#     for x,y in choice:
#         val = grid[x-1][y-1] + grid[y-1][x-1]
#         arr.append(val)
#     arr.sort()
#     for i in range(len(arr)-1):
#         diff = abs(arr[i+1] - arr[i])
#         if diff < min_abs:
#             min_abs = diff
#     print(f'#{t}',min_abs)
