
"""
Write a function:

def solution(A)


that, given an array A consisting of N integers, returns the maximum sum of two numbers
whose digits add up to an equal sum. If there are no two numbers whose digits have an equal
sum, the function should return -1


Examples:

1. Given A = [51, 71, 17, 42], the function should return 93. There are two pairs of numbers
whose digits add up to an equal sum: (51, 42) and (17, 71). The first pair sums up to 93.

2. Given A = [42, 33, 60], the function should return 102. The digits of all numbers in A add up
to the same sum, and choosing to add 42 and 60 gives the result 102.

3. Given A = [51, 32, 43], the function should return -1, since all numbers in A have digits that
add up to different, unique sums.

Write an efﬁcient algorithm for the following assumptions:


- N is an integer within the range [1 ..200,000];
- each element of array A is an integer within the range [1 ..1,000,000,000].
"""

def solution(A):
    list_summ = []
    summ = 0
    max_summ = -1

    for a_int in A:
        for digit in str(a_int):
            summ += int(digit)
        list_summ.append(summ)
        summ = 0

    for index in range(len(list_summ)):
        cur_value = list_summ[index]
        first_index = second_index = index
        count_indexes = list_summ.count(cur_value)
        for j in range(1, count_indexes):
            if cur_value in list_summ[second_index + 1:]:
                second_index = list_summ.index(cur_value, second_index + 1)
                cur_summ = A[first_index] + A[second_index]
                if cur_summ > max_summ:
                    max_summ = cur_summ

    print(max_summ)
    return max_summ


solution([42, 33, 60])