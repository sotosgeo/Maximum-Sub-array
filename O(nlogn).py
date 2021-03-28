import random
import timeit


random.seed(1059310)

def makeArray(len,n):
    return [random.randint(-n, n) for _ in range(len)]


data_set_1 = makeArray(1000000,100)
data_set_2 = makeArray(2000000,100)



def MaxSubEvenFaster(A, left, right): 

    if left == right:
        return max(0, A[left])
    max1_start = 0
    max1_end = 0

    mid = (left + right) // 2

    left_max = 0 
    s = 0
    for i in range(mid, left - 1, -1):
        s += A[i]
        if s > left_max:
            left_max = s
            max1_start = i

    s = 0
    right_max = 0 
    for i in range(mid + 1, right + 1):
        s += A[i]
        if s > right_max:   
            right_max = s
            max1_end = i
   
 
    return max(MaxSubEvenFaster(A,left,mid),MaxSubEvenFaster(A,mid+1,right),left_max+right_max)
    
t0 = timeit.default_timer()
result_of_data_set_1 = MaxSubEvenFaster(data_set_1,0,len(data_set_1)-1)
t1 = timeit.default_timer()
dt1 = t1 - t0
t2 = timeit.default_timer()
result_of_data_set_2 = MaxSubEvenFaster(data_set_2,0,len(data_set_2)-1)
t3 = timeit.default_timer()
dt2 = t3-t2
print("O(nlogn) - Divide and Conquer - 1000000 and 2000000")
print("Data Set 1 max:",result_of_data_set_1,"in",dt1,"sec")
print("Data Set 2 max:",result_of_data_set_2,"in",dt2,"sec")




