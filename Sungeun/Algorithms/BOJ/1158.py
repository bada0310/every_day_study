# 원형으로 앉아있다는 전제 (순환 인덱스를 위해 시작 인덱스를 -1로 설정한다)
# K 번쨰 사람을 제거 (K번째 생존자를 찾아 제거하는 과정을 N-1)
# 제거된 사람 이후 부터 다시 K 번째르 세게 한다.

# list 를 이용한 풀이 
def josephus(n,k):
    res = [] # list[int] # result 를 담을 lst
    line = [1 for _ in range(n)] # 값이 1이면 제거 대상, 0이면 제거 완료
    i = -1
    for _ in range(n-1):
        count = 0 # int
        while count < k:
            i = (i + 1) % n # 계속 순환하므로 나머지 연산으로 인덱스 계산 
            if line[i]:
                count += 1
        line[i] = 0
        res.append(i+1) 
    res.append(line.index(1)+1)
    return res

print(josephus(7,3))
            
#que 로 구현해보기 
# 원형(링)에서 한 부분을 잘라서 하나의 긴 que 로 구성할 수 있도록 해본다. 
# deque 로 만든 que 는  단방향이 아닌 양방향이기 때문에 자유롭게 
# 끊고? 뽑을수 있다? 
# what?

from collections import deque
import sys
input_1 = sys.stdin.readline()
n, k = map(int,input_1.split()) #  7 3
res = [] # result 가 담기는 곳
q = deque() # 직접 구현한 쿠 클래스를 이용
# q = Queue()

for i in range(n):
    # q.enqueue(i+1)
    q.append(i+1)
while q:  # q.front.next q 가 비어있으면 False 가 나온다. 
    for _ in range(k-1):
        q.append(q.popleft()) 
    res.append(q.popleft()) 

#         q.enqueue(q.dequeue())
#     res.append(q.dequeue())
# res.append(q.dequeue())

print('<',end="")
print(*res,sep=", ",end="")
print('>',end="") 
 