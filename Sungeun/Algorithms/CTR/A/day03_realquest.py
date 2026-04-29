#day03_실전문제 
# ROG 마을
# 알바생 코디는 N×N 격자 형태로 표현되는 ROG 마을에 배달을 가게 됐습니다.
# ROG 마을은 격자의 칸들이 하나의 집을 나타내며, 집마다 R,O,G중 하나의 색이 부여되어 있습니다.
# 색이 R,O인 집으로 이동하는 것은 불가능하며 G인 집으로만 이동할 수 있습니다. 
# 초기색이 O였던 칸은 코디가 매 A번째 이동을 하기 전 다음 색으로 변경됩니다. 색이 변경되는 순서는 O→G→R→… 가 반복됩니다.
# 코디가 현재 T번째 이동을 수행한다 할 때, 이동 과정을 살펴보면 다음과 같습니다.
# T가 A의 배수라면, 초기색이 O였던 모든 칸들은 다음 색으로 변경됩니다.
# 코디가 이동 가능한 상하좌우 인접한 칸으로 이동하거나 현재 칸에 머무룹니다.
# R,O 색 칸으로 이동하는 것은 불가능하지만 머무르는 것은 가능합니다. 
# 즉, 초기색이 O였던 칸이 G로 변한 시점에서 머무르다 R,O로 바뀌는 경우에 해당 칸에서 머무르거나 인접한 G칸으로 이동하는 것이 가능합니다.

# 코디는 현재 (x1,y1) 칸에 위치해 있고, 배달 목적지는 (x2, y2) 칸입니다.
# 코디가 목적지에 도달할 수 있는 최소 이동 횟수를 출력하는 프로그램을 작성하세요. 배달 목적지에 도달이 불가능하다면 −1을 출력합니다.

# 최단이동거리 -> BFS
from collections import deque
import sys
input = sys.stdin.readline

N, A = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
x1, y1 = map(int,input().split()) # 코디의 초기 위치 
x2, y2 = map(int,input().split()) # 목적지 
visited = [[False]*N for _ in range(N)]
# R = 0 O = 1 G = 2
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
# 초기색이 O였던 칸은 코디가 매 A번째 이동을 하기 전 다음 색으로 변경 (O -> R-> G -> O 순서로 변경 !! 

def get_curr_color(r, c, time):
    ori_color = board[r][c] # 일단 색을 가져온다 
    if ori_color == 1:  # 1인 경우에만 적용 
        change_count = time//A #변환 횟수 계산 (시간의 흐름에 따라 변화간 일어난 총 횟수를 찾을수 있음)
        return (1+change_count)%3 #다음 색 결정 
    return ori_color # 1이 아닌 경우 그냥 원래대로 return 한다 

                                                                                                                                                                                                                                                                                                                                  
    
def bfs():
    queue = deque([(x1,y1,0)]) #시작점의 좌표 + time  #tuple 로 묶어야 함 
    
    visited = set([(x1, y1,0)]) # 방문 상태  #tuple 로 묶어야 함 
    
    while queue:
        curr_x, curr_y, time = queue.popleft() # 이전데이터를 제거 (현재내 위치, 시간 )
        
        if curr_x == x2 and curr_y == y2:
            return time # 이때의 최종 이동횟수 (시간) 을 출력 
        
        next_time = time + 1 #이동시 count 
        # 그리고 이동하지 않더라도 count (대기상태)
        # change_count = next_time//A # 변화량 계산 
        
        for dx, dy in [(0,1), (1,0),(0,-1),(-1,0)]: # 이동시도 
            nx, ny =curr_x + dx, curr_y + dy
            
            if 0<= nx < N and 0<= ny < N:
                next_color = get_curr_color(nx, ny, next_time)# R = 0 O = 1 G = 2
                
                if next_color == 2:
                    state = (nx, ny, next_time % (A*3))
                    if state not in visited:
                        visited.add(state)
                        queue.append((nx,ny, next_time))
                        
        # 대기할동안 
        wait_state = (curr_x, curr_y, next_time%(A*3))
        if wait_state not in visited:
            visited.add(wait_state)
            queue.append((curr_x, curr_y, next_time))
    return -1

print(bfs())