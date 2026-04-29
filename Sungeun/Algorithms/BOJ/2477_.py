#2477 # 신발끈 공식? 
import sys
n = int(input()) # 1m^2 안에 있는 참외의 갯수 
 # [[4, 50], [2, 160], [3, 30]]

lst_pos = []
pre_pos =[0,0]
for _ in range(6):
    dir, length = map(int,input().split())
    if dir == 4: # 북쪽
        pre_pos = [a + b for a, b in zip(pre_pos,[0,length])]
        lst_pos.append(pre_pos)

    if dir == 3: # 남쪽 
        pre_pos = [a + b for a, b in zip(pre_pos,[0, -length])]
        lst_pos.append(pre_pos)

    if dir == 2: # 서쪽 
        pre_pos = [a + b for a, b in zip(pre_pos,[-length, 0])]
        lst_pos.append(pre_pos)

    if dir == 1: # 동쪽 
        pre_pos = [a + b for a, b in zip(pre_pos,[length, 0])]
        lst_pos.append(pre_pos)
        
# 신발끈 공식을 구현
# lst_pos = [[a,b], [c,d]...... ] 이렇게 존재할 예정 
sum_a = 0
sum_b = 0
for i in range(len(lst_pos)-1):
    sum_a += lst_pos[i][0]*lst_pos[i+1][1]
    sum_b += lst_pos[i][1]*lst_pos[i+1][0]
    result = (sum_a - sum_b)//2
print(result*n)