# 방향에 맞추어 이동
# (0, 0)에서 시작하여 총 N번 움직여보려고 합니다. 
# N번에 걸쳐 움직이려는 방향과 움직일 거리가 주어졌을 때, 최종 위치를 출력하는 프로그램을 작성해보세요.
# 단, dx, dy 테크닉을 활용하여 문제를 해결해주세요.

n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x, y = 0, 0 #초기위치는 지정해줘야 한다. 
for dir, dist in moves:
    move_dist = int(dist)
    if dir == 'N':
        y += move_dist
    if dir == 'W':
        x -= move_dist
    if dir == 'S':
        y -= move_dist
    if dir == 'E':
        x += move_dist
    
print(x, y)

# 문자에 따른 명령
# (1, 5) 위치에서 시작하며 현재 북쪽을 바라보고 있습니다. 

# 방향을 시계방향으로 90' 회전한 후, 
# 앞으로 한 칸 이동한 이후의 위치를 구해보세요.

dirs = input()

# Please write your code here.
x, y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

current_dir = 0 # 북쪽을 보고 있다 가정 
          
for cmd in dirs:
    if cmd == 'L':
        current_dir = (current_dir - 1)%4
    elif cmd == 'R':
        current_dir = (current_dir + 1)%4
    elif cmd == 'F':
        x += dx[current_dir]
        y += dy[current_dir]
print(x, y)