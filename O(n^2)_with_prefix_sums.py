import random
import timeit


random.seed(1059310)

def makeArray(len,n):
    return [random.randint(-n, n) for _ in range(len)]

data_set_test = makeArray(100,100)
data_set_1 = makeArray(5000,100)
data_set_2 = makeArray(10000,100)
small_test = [-2,-4,3,-1,5,6,-7,-2,4,-3,2]

def MaxSubFaster(A):
    t0 = timeit.default_timer()
    n = len(A)
    prefix_sums = []
    prefix_sums.append(A[0])
    for i in range(1,n):
        prefix_sums.append(prefix_sums[i-1]+A[i])
    max1 = 0
    for j in range(n):
        for k in range(j,n):
            s = prefix_sums[k] - prefix_sums[j]
            if s > max1:
                max1 = s
                max_1_start = j
                max1_end = k
    t1 =timeit.default_timer()            
    return max1,max_1_start,max1_end,t1-t0
   
result_of_data_set_1 = MaxSubFaster(data_set_1)
result_of_data_set_2 = MaxSubFaster(data_set_2)
print("O(n^2) with prefix sums")
print("Data Set 1 max:",result_of_data_set_1[0],"starting in position",result_of_data_set_1[1],"and ending in position ",result_of_data_set_1[2],"in",result_of_data_set_1[3],"sec")
print("Data Set 2 max:",result_of_data_set_2[0],"starting in position",result_of_data_set_2[1],"and ending in position ",result_of_data_set_2[2],"in",result_of_data_set_2[3],"sec")

