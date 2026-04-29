from collections import deque 
import sys
input = sys.stdin.readline
n = int(input())
que = deque()
result = []
for _ in range(n):
    line = input().split()
    if not line: continue 
    cmd = line[0] 

    if cmd == 'push':
        que.append(int(line[1]))
        
    elif cmd == 'pop':
        if que:
            result.append(str(que.popleft()))
        else:
            result.append("-1")
            
    elif cmd == 'front':
        if  que:
            result.append(str(que[0]))
        else:
            result.append("-1")
        
    elif cmd == 'back':
        result.append(str(que[-1] if  que else "-1"))
        
    elif cmd == 'size':
        result.append(str(len(que)))
        
    elif cmd == 'empty':
        result.append(str("0" if que else "1"))
        
print("\n".join(result))
