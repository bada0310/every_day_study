# 10811
n, m = map(int,input().split())
# n = lst 원소 갯수 m = 명령의 수 
lst_num = list(range(1,n+1)) # lst원소 
for _ in range(m):
    x , y= map(int,input().split()) #
    lst_num[x-1:y] = lst_num[x-1:y][::-1]
    
print(*lst_num,sep=' ')