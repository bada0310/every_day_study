from collections import deque

def calculate(N,M): # bfs
    q = deque([(N,0)]) # 현재 숫자 연산 횟수
    visited = set()
    visited.add(N)

    while q:
        curr_num , curr_cnt  = q.popleft()
        
        # 종료 조건
        if curr_num == M:
            return curr_cnt
        
        next_cal = [curr_num +1, curr_num -1, curr_num *2, curr_num -10]
        for next_num in next_cal:
            if 0<= next_num <= 1000000:
                if next_num not in visited:
                    visited.add(next_num)
                    q.append((next_num, curr_cnt +1))
    return -1
T = int(input())

for tc in range(1,T+1):
    N , M  = map(int,input().split())
    # +1, -1, *2, -10 연산 
    # 최소 몇번의 연산 
    ans = calculate(N,M)
    print(f'#{tc}',ans)