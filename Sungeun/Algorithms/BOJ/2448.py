def min_star(height):
    res = []
    for i in range(1, height + 1):
        space = ' '*(height-i) # append 에는 end= " "가 적용됮 ㅣ않아서
        if i == height:
            line = space + "*" * (2 * i - 1)
        elif i > 1:
            line = space + '*' + ' ' * (2 * i - 3) + '*'
        else: # i == 0
            line = space + '*'
        line = line + space
        res.append(line)
    return res
        
def star(N):
    if N == 3:
        return min_star(3)
    curr_star = star(N//2)
    
    result = []
    
    for s in curr_star:
        result.append(' '*(N//2) + s + ' '*(N//2))
    
    for s in curr_star:
        result.append(s + " " + s)
        
    return result
N = int(input())
print('\n'.join(star(N)))

# height = 3
# for i in range(1, height + 1): 
#     print(' ' * (height - i), end = "")

#     if i == height:
#         print("*" * (2 * i - 1))

#     elif i > 1:
#         print('*' + ' ' * (2 * i - 3) + '*')

#     else:
#         print('*')