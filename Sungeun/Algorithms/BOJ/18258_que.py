n = int(input())
que =[]
for _ in range(n):
    line = input().split() # push 1  이라면 lines=['push', 1]
    if not line: continue 
    
    cmd = line[0]
    # 명령어 push/ pop/ front/ back/ size / empty 
    if cmd == 'push':
        que.append(int(line[1]))
        
    elif cmd == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop(0)) 
            
    elif cmd == 'front':
        print(que[0] if  que else -1)
        
    elif cmd == 'back':
        print(que[-1] if  que else -1)
        
    elif cmd == 'size':
        print(len(que))
        
    elif cmd == 'empty':
        print(0 if que else 1)
        # if len(que) > 0:
        #     print(1)
        # else:
        #     print(0)
