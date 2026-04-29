# 거울에 레이저 쏘기 2
n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
# 핀볼? 
# 북남서동 
direction = (k-1)//n # 0123 
start_count = -((k-1)%n) if (k-1)//(n*2) else (k-1)%n 
# 대각선(상좌우하)을 기준으로, 반시계로 돌기 때문에 123,456 은 양수 789, 101112 는 음수 의 영역이라 
# - 를 붙이고 계산 ? 

is_ver = False if direction % 2 else True  # 

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1] # delta

now_pos = [[0,0],[0,n-1],[n-1,n-1],[n-1,0]][direction]
if now_pos[0] == now_pos[1]:
    now_pos[1] += start_count
else:
    now_pos[0] += start_count

cnt =0
while 0<= now_pos[0] <n and 0 <= now_pos[1] < n:
    cnt += 1
    temp = 1 if (grid[now_pos[0]][now_pos[1]] == '\\') ^ (is_ver) else -1
    # X or 
    direction += temp
    direction %=4

    now_pos[0] += dr[direction]
    now_pos[1] += dc[direction]
    is_ver = not is_ver

print(cnt)

