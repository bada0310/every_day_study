from collections import deque
import sys
input_1 = sys.stdin.readline()
n, k = map(int,input_1.split()) #  7 3
res = [] # result 가 담기는 곳
q = deque() # 직접 구현한 쿠 클래스를 이용

for i in range(n):
    q.append(i+1)
while q:
    for _ in range(k-1):
        q.append(q.popleft())
    res.append(q.popleft())

print('<'+", ".join(map(str, res))+'>',end="")
# emutable 한 친구들은 재할당 why?
# value 값이 들어있는 메모리의 주소를 가리키는 주소를 (이중포인터) 16bit
# 세그먼트 트리 
# https://velog.io/@ashooozzz/Python-%EC%84%B8%EA%B7%B8%EB%A8%BC%ED%8A%B8-%ED%8A%B8%EB%A6%AC-Segment-Tree


      