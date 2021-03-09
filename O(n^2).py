import random
import timeit


random.seed(1059310)

def makeArray(len,n):
    return [random.randint(-n, n) for _ in range(len)]


data_set_1 = makeArray(8000,100)
data_set_2 = makeArray(16000,100)


def MaxSubFaster_no_sums(A):
    t0 = timeit.default_timer()
    n = len(A)
    max1 = 0
    
    for i in range(n):
        s = 0
        for j in range(i,n):
            s = s + A[j]
            if s > max1:
                max1 = s
                max1_start = i
                max1_end = j
    t1 = timeit.default_timer()
    return max1,max1_start,max1_end,t1-t0


result_of_data_set_1 = MaxSubFaster_no_sums(data_set_1)
result_of_data_set_2 = MaxSubFaster_no_sums(data_set_2)
print("O(n^2) without prefix sums - 2000 and 4000")
print("Data Set 1 max:",result_of_data_set_1[0],"starting in position",result_of_data_set_1[1],"and ending in position ",result_of_data_set_1[2],"in",result_of_data_set_1[3],"sec")
print("Data Set 2 max:",result_of_data_set_2[0],"starting in position",result_of_data_set_2[1],"and ending in position ",result_of_data_set_2[2],"in",result_of_data_set_2[3],"sec")





