# 숫자가 가장 큰 인접한 곳으로 동시에 이동

# 동시에 이동 > 시작점 list idx번의 것을 이동시키는 함수를 정의
# def find_max_dir(grid,r,c)
    # dx, dy  탐색 > 상하 좌우 순서로 탐색 
    # 큰값으로 nx, ny 로 대체하기 
    
# 2. 이동된 점들 비교하기 
# 겹쳐진 위치 있으면 둘다 삭제 > 애당초에 같은게 있으면 append 를 하지 않는다. 
# else 면 append 

# 최종 list 의 길이 = 남은 구슬의 수 

N, M, T = map(int, input().split()) # 격자크기 N  구슬 M 시간을 나타내는 T
# Create n x n grid
grid = [list(map(int, input().split())) for _ in range(N)]

# Get m marble positions
marbles = [] # 빈 리스트 필요 
for _ in range(M):
    r, c = map(int, input().split())
    marbles.append((r - 1, c - 1)) # 0-based 로 변환된 구슬의 위치 1행 1열 부터 시작하기 때문에 -1 해주어야 함 
    
def find_max_dir(grid,r,c):
    dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
    max_val = -float('inf')
    best_nx, best_ny = -1, -1 # 초기값 설정 
    for dx, dy in dir:
        nx, ny = r + dx, c + dy # 탐색 
        if 0<= nx < N and 0<= ny < N :
            if grid[nx][ny] > max_val: # 최댓값 갱신 
                max_val = grid[nx][ny]
                best_nx, best_ny = nx, ny # 최댓값 입력 
        
    return best_nx, best_ny  # 최대 좌표를 반환 



for t in range(T):
    next_pos_counts= {} # 이동된 점들의 위치가 저장 될 dict 
    
    for  r, c in marbles:
        nx, ny = find_max_dir(grid,r, c) # 모든 구슬에 대해서 함수 시행 
        
        if (nx,ny) not in next_pos_counts:
            next_pos_counts[(nx,ny)] = 1 # 만약 존재하지 않는다면 넣기 
        else:
            next_pos_counts[(nx,ny)] += 1 # 존재하면 그냥 더해주기 
            
    next_marbles = [] # 정답리스트 
    for pos, count in next_pos_counts.items():
        if count == 1: # 여기서 dict 의 val  이 1인 친구들만 모으기 
            next_marbles.append(pos) # 다시 정답 리스트에 append 
    marbles = next_marbles # 처음에 받았던 구슬(겹처진거 사라지고, 남은 구슬들 가지고 시간에 따라서 또 이동시키기)
    
print(len(marbles)) # 최종 길이 = 최종 남은 구슬들의 갯수 