# R reverse # D delete

from collections import deque
T = int(input())
for t in range(T):
    commands = input().strip()
    N = int(input())
    item = input().strip()
    # arr = list(map(int,item.strip('[]').split(',')))
    if N == 0:
        q = deque()
    else:
        q = deque(item.strip('[]').split(','))

    # 플래그 세우기!
    is_rev = False
    is_error = False
    
    for cmd in commands:
        if cmd == 'R': # reverse
            is_rev = not is_rev
        elif cmd == 'D':
            if not q: # 아예 없으면 
                is_error =True
                print('error')
                break # 종료 
            
            if is_rev: # D 인데 rev deq 이면 
                q.pop()
            else:
                q.popleft()
    if not is_error:
        if is_rev:
            q.reverse()
        print('[' + ','.join(q) + ']')

# 투포인터의 경우
# 조건: 순서 변경이 없어야함
# 출력물이 reverse 라고 하더라도, 이거는 뒤에서 출력하는 방식 
# (변수의 순서가 바뀌면 못쓰는 테크닉)

# 동적 삽입, 삭제는 항상 오버헤드가 크다..(resize 문제)
# 해시 테이블을 제외하고는 탐색알고리즘은 똥이다..    
# 이미 최대 범위를 알고있고 메모리 감당가능하다면 정적할당을 항상 고려할것!! 