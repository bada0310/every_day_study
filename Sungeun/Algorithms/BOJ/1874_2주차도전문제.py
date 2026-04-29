N = int(input())
copy_list = [int(input()) for _ in range(N)]

box_1 = []
box_2 = []
answer = [] # + - 만들어가는 리스트 
idx = 0
for k in range(1, N+1):
    box_1.append(k)
    answer.append('+')
    while box_1 and box_1[-1] == copy_list[idx]: # 같으면 box_2 lst 로 옮기기 
        idx += 1
        box_1.pop()
        answer.append('-')

if len(box_1) != 0:
    print('NO')
else:
    for i in range(len(answer)):
        print(answer[i])


        

            
            