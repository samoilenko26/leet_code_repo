
'''
Write a function

def solution(A)

that, given an array A consisting of N integers, returns the biggest value X, which occurs in A
exactly X times. If there is no such value, the function should return 0.

Examples:
1. Given A = [3, 8, 2, 3, 3, 2], the function should return 3. The value 2 occurs exactly two times
and the value 3 occurs exactly three times, so they both meet the task conditions. The value 8
occurs just once, thus it does not meet the task conditions. The maximum of 2 and 3 is 3.
2. Given A = [7, 1, 2, 8, 2], the function should return 2. The value 1 occurs exactly one time; the
value 2 occurs exactly two times.
3. Given A = [3, 1, 4, 1, 5], the function should return 0. There is no value which meets the task
conditions.
4. Given A = [5, 5, 5, 5, 5], the function should return 5.
Write an efficient algorithm for the following assumptions:

   • N is an integer within the range [1..100,000];
   • each element of array A is an integer within the range [1..1,000,000,000].
Copyright 2009-2022 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure
prohibited.

'''

def solution(A):
    result = 0
    for i in A:
        if A.count(i) == i and i > result:
            result = i
    return result

solution([3,8,2,3,3,2])