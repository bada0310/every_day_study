# 2847
# 1 만큼 감소 시키는 것이 1번이다 
# 몇번 감소 시키면 되는지 
n = int(input())
1<= n <= 100

score =[] 
count = 0
for _ in range(n):
    score.append(int(input()))
    

for i in range(n-2,-1,-1):
        if score[i]>= score[i+1]:
            target = score[i+1]-1
            diff = score[i] - target
            score[i] = target
            count += diff    
print(count)