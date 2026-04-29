from collections import deque
N = int(input())
q = deque(list(range(1, N+1)))
while q:
    temp  =q.popleft()
    q.rotate(-1)
print(temp)