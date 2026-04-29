#day03_quest
# 금채굴하기 
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
profit = 0 # 최종 이익 

# 마름모 탐색 
def finder_dia(x, y, k): #행렬탐색 중심 x, y 너비 k
    gold = 0
    for i in range(n):
        for j in range(n):
            if abs(x-i)+ abs(y-j) <= k: 
                #가로 세로 중심점으로 부터 거리 의 합이 k 이면 마름모 형태를 찾을 수 있다. 
                
                gold += grid[i][j]
    return gold

def cost(k):
    return k * k + (k+1)*(k+1) # k^2 + (k+1)^2

for k in range(n+2):
    c = cost(k)
    for i in range(n):
        for j in range(n):
            res = finder_dia(i,j,k) # 매개변수 재할당 
            if (res * m) >= c and profit < res:
                profit = res

print(profit)

# 시간 복잡도가 너무 크다 O(N^5)
# 중복으로 더해지고 있는 값이 있는지 확인 하기 
# range 의 범위를 늘려 넓게 탐색 모든 점을 다 포함하려면 마름모가 격자보다 커져아
# 할 경우가 있다 