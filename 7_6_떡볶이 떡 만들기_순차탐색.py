
total= [0]*n
h=0
# def binary_search(array,target,start,end):
#     while start <= end:
#         h= (start+end)//2
#         if target == array[h]:
#             return h
#         elif target > array[h]:
#             start=h+1
#         else:
#             end= h-1
#     return None

while sum(total)!= m:
    for i in range(len(array)):
        total[i]=array[i]-h 
        if sum(total)==m:
            break
    h=h+1
print(h)

        