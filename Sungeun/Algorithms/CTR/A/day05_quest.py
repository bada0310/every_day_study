# 단 한 번의 2048 시도 
# 이동 방향에 같은 숫자가 있으면 합으로 합친다 
# [list(rows) for rows in  zip(*grid)]
# list(zip(*grid))
# 1. 이동  (or 회전 ) 
grid = [list(map(int, input().split())) for _ in range(4)]
dir = input()

# 좌우 반전
def reversed_board(board):
    return [row[::-1] for row in board]
# 상하 반전 
def transpose_board(board):
    return[list(row) for row in zip(*board)]
# 왼쪽으로 밀고 합치는 함수                  
def move_left(board):
    new_board = []
    for row in board: # 각 행에 대헛 처리할수 있또록 하기 
        nums = [ i for i in row if i != 0] 
        merged = [] # 연산이 끝난 값을 넣을 리스트 
        skip =False  # 방금 합치기에 사용된 '뒷숫자'는 다음 검사에서 무시하라
        for i in range(len(nums)):
            if skip:
                skip = False 
                continue
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                merged.append(nums[i]*2)
                skip = True
            else:
                merged.append(nums[i])
        while len(merged) < len(row):
            merged.append(0) 
        new_board.append(merged)
    return new_board

def move(board,dir):
    if dir == 'L':
        return move_left(board)
    
    elif dir =='R':
        board = reversed_board(board)
        board = move_left(board)
        return reversed_board(board)
    elif dir == 'U':
        board = transpose_board(board)
        board = move_left(board)
        return transpose_board(board)
    elif dir == 'D':
        board = transpose_board(board)
        board = reversed_board(board)
        board = move_left(board)
        board = reversed_board(board)
        return transpose_board(board)
               
answer = move(grid, dir)
for row in answer:
    print(*row)
            

        