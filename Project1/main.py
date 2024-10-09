from copy import deepcopy
from math import inf

field_size = int(input())

field = []
for i in range(field_size):
    single_row = list(input().split())
    field.append(single_row)

test_field_1 = [
    [1, 10, 1, "a", 7],
    [2, 2, 4, 5, -4],
    [20, 1, -2, 7, 5],
    [1, 2, 3, "a", 5],
    [5, 2, "a", 1, 5]
]

test_field_2 = [
    [1, -2, 4, 5],
    [5, 2, 3, 1],
    [3, -2, 4, "a"],
    [1, 8, "a", 5],
]


path = deepcopy(field)

for i in range(len(path)):
    for j in range(len(path[i])):
        if path[i][j] == "a":
            path[i][j] = -inf
        else:
            path[i][j] = int(path[i][j])


# initialize first row of path
for j in range(1, field_size):
    path[0][j] = path[0][j-1] + path[0][j]

# initialize first column of path
for i in range(1, field_size):
    path[i][0] = path[i-1][0] + path[i][0]

# calculate maximum cost for each position
for i in range(1, field_size):
    for j in range(1, field_size):
        path[i][j] = max(path[i-1][j], path[i][j-1]) + path[i][j]
        # if path[i-1][j] > path[i][j-1]:
        #     path[i][j-1] = 0
        # else:
        #     path[i-1][j] = 0


sonic_moves = []

# print(path)

k = 0
m = 0

flag = false
while true:
    # print(path[k][m], "-------")

    if path[k][m] < 0:
        flag = true
        break
    if m == field_size - 1 and k == field_size - 1:
        break
    if k == field_size - 1:
        for a in range(0, field_size - 1 - m):
            sonic_moves.append("r")
            if path[k][a+m] < 0:
                flag = true
        break
    elif m == field_size - 1:
        for a in range(0, field_size - 1 - k):
            sonic_moves.append("d")
            if path[a+k][m] < 0:
                flag = true
        break
    if path[k][m+1] > path[k+1][m]:
        sonic_moves.append("r")
        m += 1
    else:
        sonic_moves.append("d")
        k += 1


# sonic_moves = sonic_moves[::-1]
#
# reverse_moves = []
#
# for i in sonic_moves:
#     if i == 'l':
#         reverse_moves.append('r')
#     else:
#         reverse_moves.append('d')

# print(flag)

print(path)
for row in path:
    print(row)


row = 1
col = 1
index_moves = [[1, 1]]
for i in sonic_moves:
    if i == 'r':
        col += 1
        index_moves.append([row, col])
    else:
        row += 1
        index_moves.append([row, col])

if flag or path[field_size - 1][field_size - 1] < 0:
    print("impossible")
else:
    print(path[field_size - 1][field_size - 1])
    for i in index_moves:
        print(i)


"""
4
1 -2 4 5
5  2 3 1
1 1 1 0
1  0 1 5
"""

"""
5
1 10  4  a  7
2  2  4 -3  -4
a -1  2  4  5
1  2  3  4  5
5  5  a  1  5 
"""

"""
function findsubsetswithsum(set, targetsum):
    subsets = []
    
    function backtrack(currentsubset, currentindex, currentsum):
        if currentsum == targetsum:
            subsets.append(currentsubset)
            return
        
        if currentindex >= length(set):
            return
        
        backtrack(currentsubset + [set[currentindex]], currentindex + 1, currentsum + set[currentindex])
        backtrack(currentsubset, currentindex + 1, currentsum)
    
    backtrack([], 0, 0)
    
    return subsets
"""

































