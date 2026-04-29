# 요리사
def calcul(team):
    score = 0
    for i in range(N//2):
        for j in range(N//2):
            score += grid[team[i]][team[j]]
    return score

def comb(depth, start):
    if depth == N//2:
        teams.append(res[:])
        return
    for i in range(start,N):
        res.append(i)
        comb(depth+1,i+1)
        res.pop()

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    min_val = float('inf')
    teams = [] # 전체 조합의 모든 경우
    res =[] # 한 조합의 경우 
    comb(0,0)
    for teamA in teams:
        teamB = []
        for i in range(N):
            if i not in teamA:
                teamB.append(i)
        
        scoreA = calcul(teamA)
        scoreB = calcul(teamB)     
        diff = abs(scoreA-scoreB)
        if diff < min_val:
            min_val = diff

    print(f'#{tc}',min_val)