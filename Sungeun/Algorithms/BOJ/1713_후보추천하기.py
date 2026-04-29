#1713
n = int(input()) # 3
k = int(input()) # 9 
lst_people = list(map(int,input().split()))  # 2 1 4 3 5 6 2 7 2
# lst_stack = [] # 3 까지 lst_people 의 요소가 들어갈 리스트 
dict_num = {}   

# val 이 0 이면 존재하지 않는다고 가정
for i in range(k):
    current = lst_people[i]
    
    if current in dict_num:  
        dict_num[current] += 1
    else:
        if len(dict_num) >= n:
            keys_to_remove = [k for k, v in dict_num.items()]
            if keys_to_remove:
                target_key = sorted(dict_num.items(), key=lambda x: x[1])[0][0]
                dict_num[target_key] = 0
            dict_num = {k: v for k, v in dict_num.items() if v != 0}
        dict_num[current] = 1        
                
final_keys = sorted(dict_num.keys())
print(*final_keys)
  

 


# for i in range(k): # 0~8(1~9)
#     if len(dict_num) < 3: # 3칸이 다 안찼을때
#         dict_num[lst_people[i]] = 1 # 2 의 (key) : 1 (val)
#         # clean_dict = {k: v for k, v in dict_num.items() if v != 0}     
#     elif len(dict_num) == 3: # 3 칸이 다 찼을 때 
#             if lst_people[i] in dict_num:
#                 dict_num[lst_people[i]] += 1
#             elif lst_people[i] not in dict_num :
#                 # : # dict_num 의 key 값을 탐색 존재하는지 확인 존재하지 않는다면
#                 keys = [k for k, v in dict_num.items() if v == 1]
#                 dict_num[keys[0]] = 0 # 존재하지 않는 것으로 바꿈 
#     dict_num = {k: v for k, v in dict_num.items() if v != 0}  # val = 0 인것은 주기적으로 갱신 
           
# #                
# # clean_dict = {k: v for k, v in sort_dict.items() if v != 0} 
# sort_dict = dict(sorted(dict_num.items(), key=lambda x: x[1], reverse=True))             
# print(*sort_dict.keys()) 
