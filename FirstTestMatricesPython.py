#a * det(a_minor) - b * det(b_minor) + c * det(c_minor) # det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)
#? My first try ever at real math and python before learning linear algebra !

#------------------------------
#? Short, Logical and (very sufficient) efficient coin change alg (see AntnotesVideos p.1)
def coin_change(n, coins):
    parts = [1]+[0]*n
    for c in coins:
        for i, x in enumerate(range(c, n+1)):
            parts[x] += parts[i]
    return parts[n]
#------------------------------

import itertools as it
import numpy as np
def minors_ix(m):
    N = [i for i in range(len(m))]
    for c,ix in enumerate(list(it.product(*[N,N]))):
        if c == len(m):
            return
        else:
            yield ix

def MultiDimArr(N,arr):
    for i in range(0, len(arr), N):  
        yield arr[i:i + N]

def alt_sum(iterator):
    new = []
    for c,e in enumerate(iterator):
        if c % 2 == 0:
            new.append(str(e))
        else:
            if "-" in str(e):
                new.append(str(e)[1:])
            else:
                new.append("-" + str(e)[:])
    return sum(list(map(int,new[:])))#instead of eval with str 

def delrowcol(x,y,m):
    N,length = [i for i in range(len(m))],len(m)  * [len(m)]
    ix = list(it.product(*[N,N]))
    new_ix = [p for p in ix if not (p[0] == x or p[1] == y)]
    new_mat = [m[tup[0]][tup[1]] for tup in new_ix]
    return list(MultiDimArr(len(m)-1,new_mat)) 

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    else:
        bases_ix = list(minors_ix(matrix))
        bases = [matrix[tup[0]][tup[1]] for tup in bases_ix]
        dets = [determinant(delrowcol(tup[0],tup[1],matrix)) for tup in bases_ix] #!recursion here
        pros = [b*d for b,d in zip(bases,dets)]
        return alt_sum(pros)

m1 = [ [1, 3], [2,5]]
m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]
m3 = [[4,5,7,1],[4,7,-7,4],[4,3,-1,-2],[-9,6,7,2]]
print(determinant(m3))

# [[7, -7, 4], [3, -1, -2], [6, 7, 2]]
# [[-1, -2], [7, 2]]
# [[3, -2], [6, 2]]
# [[3, -1], [6, 7]]
# [12, 18, 27] [7, -7, 4] BRUH
# [[4, -7, 4], [4, -1, -2], [-9, 7, 2]]
# [[-1, -2], [7, 2]]
# [[4, -2], [-9, 2]]
# [[4, -1], [-9, 7]]
# [12, -10, 19] [4, -7, 4] BRUH
# [[4, 7, 4], [4, 3, -2], [-9, 6, 2]]
# [[3, -2], [6, 2]]
# [[4, -2], [-9, 2]]
# [[4, 3], [-9, 6]]
# [18, -10, 51] [4, 7, 4] BRUH
# [[4, 7, -7], [4, 3, -1], [-9, 6, 7]]
# [[3, -1], [6, 7]]
# [[4, -1], [-9, 7]]
# [[4, 3], [-9, 6]]
# [27, 19, 51] [4, 7, -7] BRUH
# ([318, 124, 346, -282], [4, 5, 7, 1])
#--------------------
#!SUMMATIONS PHYSICS FUN
#?CW force on particule in single unit of matrix K x N: 1 /( k * (n+1)^2k )
     
#? lots of tries with partial sums and gaussians definitions of summations 