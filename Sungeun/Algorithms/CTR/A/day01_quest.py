# 되돌아오기 
# (0, 0)에서 시작하여 총 N번 움직여보려고 합니다. N번에 걸쳐 움직이려는 방향과 움직일 거리가 주어지고, 
# 1초에 한 칸씩 움직인다고 했을 때, 몇 초 뒤에 처음으로 다시 (0, 0)에 돌아오게 되는지를 판단하는 프로그램을 작성해보세요.

N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x, y = 0, 0
time = 0
returned = False
dx = {'N': 0, 'E': 1, 'S': 0, 'W': -1}
dy = {'N': 1, 'E': 0, 'S': -1, 'W': 0}

for move_dir, move_dist in moves:
    dist = int(move_dist)

    for _ in range(dist):
        x += dx[move_dir]
        y += dy[move_dir]
        time += 1
        if x == 0 and y == 0:
            print(time)
            returned = True
            break
    if returned:
        break
        
if not returned:
    print(-1)