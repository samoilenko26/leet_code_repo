
"""
An English text needs to be encrypted using the following encryption scheme.

Sample Input
have a nice day

Sample Output
hae and via ecy

Explanation
length = 12 (without spaces), sqrt(12) is between 3 and 4.
rows in 3, and columns in 4
Rewritten with  rows and  columns:

have
anic
eday

Resolving:

import math
s=input()
sm=s.replace(" ","")
r=math.floor(math.sqrt(len(sm)))
c=math.ceil(math.sqrt(len(sm)))
for i in range(c):
    print(sm[i::c],end=" ")

"""

import math

def encryption(string):
    string = string.strip().replace(' ', '')
    length = len(string)
    root = math.sqrt(length)
    rows = math.floor(root)
    columns = math.ceil(root)

    tmp_result = []
    tmp_index = 0
    tmp_dict = {}

    # result = [string[rows * i : rows * i + rows] for i in range(columns)]
    while True:
        tmp_string = string[tmp_index : tmp_index + columns]
        tmp_index += columns
        if tmp_string == '':
            break
        else:
            tmp_result.append(tmp_string)
            for i in range(len(tmp_string)):
                if i in tmp_dict:
                    tmp_dict[i] += tmp_string[i]
                else:
                    tmp_dict[i] = tmp_string[i]
    result = ' '.join(list(tmp_dict.values()))
    print(result)
    return result

encryption("iffactsdontfittotheorychangethefacts")
