
'''
  You are given a string S containing lowercase English letters. our task is to calculate the
  minimum number of letters that need to be removed in order to make it possible to build a
  palindrome from the remaining letters. When building the palindrome, you can rearrange the
  remaining letters in any way.

  A palindrome is a string that reads the same both forwards and backwards. Some examples

  of palindromes are: "kayak", "radar", "mom".

  Write a function:


       def solution(S)

  which, given a string of length N, returns the minimum number of letters that need to be
  removed.

  Examples:

  1. Given S = "ervervige", your function should return 2. After removing the letter "g" and one "e",
  we may create a word "reviver", which is a palindrome.

  2. Given S = "aaabab", your function should return 0. We may create a word "aabbaa", which is
  a palindrome and uses all of the letters.                                                 II

  3. Given S = "x", your function should return 0. String "x" is a palindrome itself, so we do not
  have to delete any letter.

  Write an efficient algorithm for the following assumptions:

       • N is an integer within the range [1..200,000];
       • S contains only lowercase English letters.
'''


def permutations(string, step, result):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        result.append(''.join(string))

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1, result)

def solution(A):
    result = []
    step = 0
    permutations(A, step, result)

    step = 0
    while step != len(result[0]):
        for string in result:
            if string[step:] == string[step:][::-1]:
                print(step)
                print(string[step:])
                return step
        step += 1

solution("anaannna1")

