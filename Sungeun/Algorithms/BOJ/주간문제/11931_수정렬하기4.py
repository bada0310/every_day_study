# O(N \log N)
# 병합 정렬 (Merge Sort) / 힙 정렬 (Heap Sort) / 퀵 정렬 (Quick Sort)
# 퀵정렬은 안됌 

def heapify(arr, idx, heap_size):
    largeset = idx
    left = 2 *  idx  + 1
    right = 2 * idx + 2 

    if left < heap_size and arr[left] < arr[largeset]:
        largeset =left
    if right < heap_size and arr[right] < arr[largeset]:
        largeset = right 
    if largeset != idx:
        arr[largeset], arr[idx] = arr[idx], arr[largeset]
        heapify(arr,largeset, heap_size)

def heap_sort(arr):
    for i in range(N//2-1, -1, -1):
        heapify(arr, i, N)
    for i in range(N-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr,0,i)
    return arr

N = int(input())
arr = []
for _ in range(N):
    num = int(input())
    arr.append(num)

res = heap_sort(arr)
for i in res:
    print(i)


