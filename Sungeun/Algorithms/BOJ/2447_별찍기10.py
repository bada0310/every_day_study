#2447 별찍기 10 
N = int(input()) # 3*K 

def format(N):
    if N == 1:
        return['*']
    square = format(N//3)
    result  =[]

    for s in square:
        result.append(s*3)
    for s in square:
        result.append(s + ' '*(N//3) + s)
    for s in square:
        result.append(s*3)
    return result 
print('\n'.join(format(N)))