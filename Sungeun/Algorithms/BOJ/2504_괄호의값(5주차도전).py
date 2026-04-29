# test 1 
# arr =list(input().strip())
# stack = []
# tmp = 0
# ans = 0
# for i in range(len(arr)):
#     if arr[i] =='(':
#         tmp = 2
#     elif arr[i] =='[':
#         tmp = 3
#         if arr[i] =='(':
#             tmp *= 2
#         elif arr[i] =='[':
#             tmp *= 3
            

# print(ans)

# test 2 
arr = list(input().strip())
stack = []
tmp = 1
ans = 0
for i in range(len(arr)):
    if arr[i] =='(':
        tmp *= 2
        stack.append(arr[i])
        
    elif arr[i] =='[':
        tmp *= 3
        stack.append(arr[i])
        
    elif arr[i] ==')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if arr[i-1] == '(':
            ans += tmp
        stack.pop()
        tmp //=2 
    elif arr[i] ==']':
        if not stack or stack[-1] =='(':
            ans = 0
            break
        if arr[i-1] == '[':
            ans += tmp
        stack.pop()
        tmp//=3
if stack:
    print(0)
else:
    print(ans)