# CTR_공정한 팀 나누기 
# 스타트 앤링크 
# 요리사 문제 
N, K = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
min_diff = float('inf')
res_a = []

def calcul(res): # 1개의 조합에 대해 계산하는 함수 
    score = 0
    for i in res:
        for j in res:
            score += grid[i][j]
    return score

visited = [False]*N
def comb(depth,start):
    global min_diff
    if depth >= K:
        res_b = []
        for i in range(N):
            if i not in res_a:
                res_b.append(i)
        # prunning
        if len(res_a) >= K and len(res_b)>= K:
            diff = abs(calcul(res_a)-calcul(res_b))
            if diff < min_diff:
                min_diff = diff

    for i in range(start,N):
        if not visited[i]:
            visited[i] = True
            res_a.append(i)
            comb(depth+1, i+1)
            visited[i] = False
            res_a.pop()

comb(0,0)
print(min_diff)
    