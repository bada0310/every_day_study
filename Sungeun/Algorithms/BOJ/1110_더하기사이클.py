# 1110
start_num = int(input()) 
original_num = start_num 
count = 0 

while True: # 2+6 =8 ... 4+2 =6 , 2+6
    n = start_num // 10
    m  = start_num % 10
    k = n + m
    
    start_num = (m * 10) +(k % 10)
    count += 1
    
    if original_num == start_num:
        break 
    
print(count)