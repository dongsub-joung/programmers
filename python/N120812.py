
def solution(array: list):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0:
            return a
    return -1


# try 1
# def solution(array: list):
#     max = 0
#     for e in seted_array:
#         cnt= array.count(e) 
#         if cnt > max:
#             max= cnt
#         if e != array[idx-1] and cnt == max:
#             return -1
#         idx+=1
#     return max

# try 2
# def solution(array: list):
#     array.sort()
#     temp, max= 0, 0
    
#     for e in array:
#         if temp == e:
#             pass
        
#         cnt= array.count(e)

#         if temp != e and cnt == max:
#             return -1

#         if cnt > max:
#             max= cnt

#         temp= e
#     return max

# try 3
# def solution(array: list):
#     cnt_array=[]
#     array.sort()
#     seted_array= set(array)
#     for e in seted_array:
#         cnt_array.append(array.count(e))
    
#     max=0
#     for e in cnt_array:
#         if max < e:
#             max= e
#         if max == e:
#             return -1
#     return max
