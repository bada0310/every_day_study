#2628
n ,m = map(int,input().split()) # 최대값이 n, m 인 
cut = int(input()) # 자르는 선의 갯수
lst_n = [0,n] # 가로 리스트 
lst_m = [0,m] #세로 리스트 
if cut == 0:  # 자른 횟수가 0인 경우도 있을수도 있다? 이것도 고려해야함!! 
    print(n*m)
    exit()

# 자른 횟수만큼 input() 을 받는다. 근데 이제 가로 세로를 각각 엽력하기 
# 가로를 자른다고 하면 세로 줄에 append()
# 세로를 자른다고 하면 가로 줄에 append()
for _ in range(cut):
    a, b = map(int, input().split())  # 0 3 == 기로  3
    if a == 1:
        lst_n.append(b) # 4
    elif a == 0:
        lst_m.append(b)  # 2 3 

lst_n.sort()
lst_m.sort() # [0, 1, m ]

# 가장 긴 가로 세로 길이를 찾는 함수 
# 
max_length = 1
max_width = 1
for i in range(len(lst_n)-1):
    max_length =max(max_length,(lst_n[i+1]-lst_n[i]))
for idx in range(len(lst_m)-1):
    max_width =max(max_width,(lst_m[idx+1]-lst_m[idx]))

print(max_length*max_width)