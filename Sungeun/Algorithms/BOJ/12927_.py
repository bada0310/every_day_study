# 12927
# 스위치 문자열을 리스트로 받기 
lst_switch = list(map(str, input().strip())) # YYYYYY
count = 0
# 버튼을 누른 횟수 

#전구 스위치들의 인덱스들을 기준으로 계산한다. 
for i in range(len(lst_switch)): #idx = i 
    
    if lst_switch[i] == 'Y':
        count += 1
        # j 번쨰의 인덱스를 생각하는데 배수의 위치한 스위치도 꺼야하기 때문에 간격 i+1
        # 'Y' => 'N' 'N' => 'Y'
        for j in range(i,len(lst_switch),i+1):
            if lst_switch[j] =='Y':
                lst_switch[j] ='N'
            else: # lst_switch[j] =='N'
                lst_switch[j] = 'Y'

print(count)