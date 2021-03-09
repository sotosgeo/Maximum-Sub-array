import random
import timeit


random.seed(1059310)

def makeArray(len,n):
    return [random.randint(-n, n) for _ in range(len)]


data_set_1 = makeArray(10000000,100)
data_set_2 = makeArray(20000000,100)



def MaxSubFastest(A):
    t0 = timeit.default_timer()
    best_start = best_end = 0 
    max_sum = 0 
    s = 0
    n = len(A)
    for i in range(n):
        if s <= 0: 
            current_start = i
            s = A[i]
        else:
            s += A[i]

        if s > max_sum:
            max_sum = s
            best_start = current_start
            best_end = i   
    t1 = timeit.default_timer()
    return max_sum, best_start, best_end,t1-t0


result_of_data_set_1 = MaxSubFastest(data_set_1)
result_of_data_set_2 = MaxSubFastest(data_set_2)


print("O(n) - Kadane's Algorithm")
print("Data Set 1 max:",result_of_data_set_1[0],"starting in position",result_of_data_set_1[1],"and ending in position ",result_of_data_set_1[2],"in",result_of_data_set_1[3],"sec")
print("Data Set 2 max:",result_of_data_set_2[0],"starting in position",result_of_data_set_2[1],"and ending in position ",result_of_data_set_2[2],"in",result_of_data_set_2[3],"sec")

