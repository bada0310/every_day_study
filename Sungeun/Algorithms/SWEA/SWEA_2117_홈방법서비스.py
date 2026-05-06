# M 은 각 집이 지불해줄수 있는 금액의 단위
# 운영 비용 = K * K + (K - 1) * (K - 1)
# 운영비 < M*(집의 갯수)
# 손해를 보지 않고 서비스 가능한 최대의 집 수 

# 가장많은 집을 포함하며
# 손해를 보지 않으면서 
# grid 내에서 가장 큰 영역(종이)부터 1씩 줄여나가며 대입
# grid 큰 종이를 좌표별로 대입해가면서 1을 몇개씩 포함하고 있는지 비교 

# 그리고 비용과 집갯수*M 를 비교해서 집갯수가 
# 손해를 보지 않으면서 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾았을 때
def count_house(grid,visited):
    cnt = 0 
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1 and visited[i][j]== 1:
                cnt += 1
    return cnt 

def is_range(r,c): # N*N grid 내에 있는지 보기 
    return 0<= r < N and 0<= c < N 

def find_area(r,c): # 방범 가능한 영역 구하기 
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if abs(i-r)+ abs(j-c) <= K-1 and is_range(i,j):
                visited[i][j] = 1
    return visited

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(N)]

    max_house = 0 #손해를 보지 않을때  방범서비스르 가장 많은 집들에 제공하는 서비스 영역을 
    K = 1
    while K <= N+1:
        cost = K * K + (K - 1) * (K - 1) # 운영비용 
        for i in range(N):
            for j in range(N):
                area = find_area(i,j)
                cnt_house = count_house(grid,area)
                if M * cnt_house >= cost and cnt_house >= max_house: # 손해를 보지 않으면서 집 갯숙가 가장 많을 때 
                    max_house = cnt_house
        K += 1

    print(f'#{tc}',max_house)