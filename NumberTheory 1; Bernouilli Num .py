from FirstTestMatricesPython import * #first math alg I made before linear algebra, may use it here sometime
#Computation of Bernouilli Numbers and related subjects
#--------------------------
import timeit

#! Cool int partitions functions Notesp1
#COUNT 
def partitions_gen(n,c, I=1): 
    #global c 
    #c+=1
    c = c + 1
    yield (n, )
    for i in range(I, n//2 + 1):
        for p in partitions_gen(n-i,c, i):
            yield (i, ) + p

def partition_recur(num = int(),output = set()):
    output.add((num, )) #one el tup
    for i in range(1, num):
        for j in partition_recur(num - i):
            output.add(tuple(sorted((i, )+j,reverse= False)))
    return output

#N = input("Enter natural number: ") #!Manually change in code snippets for proper timeit -> TIME COMPLEXITY
N = 5
test1 = """
global N
N = 30
def partitions_gen(n,c, I=1):
    #global c
    #c+=1
    #c = c + 1
    #global c
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions_gen(n-i,c, i):
            yield (i,) + p
list(partitions_gen(N,0))  #!with list() ?
"""
test2 = """
global N
N = 100
def partition_recur(num = int(),output = set()):
    output.add((num, )) #one el tup
    for i in range(1, num):
        for j in partition_recur(num - i):
            output.add(tuple(sorted((i, )+j)))
    return output
len(partition_recur(N))
"""
#!print(partition_recur(N))
#!print("    Partition recursive")
#!print(timeit.timeit(stmt=test2,number=1000))

#second function  
#print(list(partitions_gen(N,0)))
#print("    Partition generator")
#print(timeit.timeit(stmt=test1,setup= "",number=1))


#!-------------------------------

#? Short, Logical and (very sufficient) efficient coin change alg (see AntnotesVideos p.1)
def coin_change(n, coins):
    parts = [1]+[0]*n
    for c in coins:
        for i, x in enumerate(range(c, n+1)):
            parts[x] += parts[i]
    return parts[n]
#!--------------------------


import math

#?print(list(pyramid(pascals_triangle(5))))
#-------------------------------------------------------------------------------------------------------------
#!---------------BERNOULLI NUMBERS----- appear in taylor series and riemann zeta function ? <-- learn and read on this

import sympy as sym
sym.init_printing(use_unicode=False, wrap_line=True)

def pyramid(arr):
    """uses summation of n partial sum testing"""
    if len(arr) <= 1:
        return "not a pyramid"
    S,l = 0,0
    while len(arr) != S:
        l += 1
        S = (l/2)*(l+1)
    print("layers: " + str(l),sep = "\t")
    n = -1
    s0 = lambda n: (n/2)*(n+1)
    s1 = lambda n: ((n+1)/2)*((n+2))
    while n != l:
        n += 1
        a = arr[int(s0(n)):int(s1(n))]
        if a:
            yield a
print(pyramid([]))

def pascals_bernoulli(n):
    Triangle = [] #@ see AntNotes page 2 for cool logic ! 
    for ix_row in range(n):
        row = [0 for _ in range(ix_row+1)]
        row[0], row[-1] = 1,(ix_row+1)
        if all(row):
            pass
        else:
            for col in range(1, len(row)-1):
                row[col] = Triangle[ix_row-1][col-1] + Triangle[ix_row-1][col]
        Triangle.append(row)
    return [i for arr in Triangle for i in arr]

#?print(list(pyramid(pascals_bernoulli(4)))) 
from sympy import *
#!example b4:    0 = 1 + 5b1 + 10b2 + 10b3 + 5b4             (in b{ix})
# equations:   
# B0 arr[0]: B[0]                 
# B1 arr[1]: 0 = B[0] + 2*x
# B2 arr[2]: 0 = B[0] + 3*B[1] + 3*x
#[...]


def bernoulli_number(n):
    arr = list(pyramid(pascals_bernoulli(n+1)))
    B = [1] #first b0 is 1
    #for x in range(1,n+1):
    for layer in arr[1:]:
        temp = []
        for c,i in enumerate(layer):
            x = sym.Symbol("x")
            if (c+1) == len(layer):
                temp.append(i * x)
                break
            else:
                temp.append(B[c]*i)
        #N([v for k,v in res.items()][0])
        res = N(sym.solve(sum(temp),(x))[0])
        B.append(res)
        res = int()
        temp.clear()
    return B[n]

#print(bernoulli_number(8),flush=False)

#-----------------------------------------------------------------
from functools import reduce
from math import factorial as fac
def factorial(n):
    """natural numbers"""
    if n == 1:
        return n
    elif n < 1:
        return 
    else:
        return n*factorial(n-1)

def binomial(x, y):
    try:
        binomial = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binomial = 0
    return binomial

def pascal(l):
    """pascal with binomial, using facotiral defintion ( binomial() )"""
    for x in range(l + 1):
        print([binomial(x, y) for y in range(x + 1)])




def comb(n, k): #! BINOMIAL COEFFICIENT MULTIPLICATIVE FORMULATION RATHER THAN FACTORIAL DEFINITION: #min(*n)
    '''
    n: size of range of elements
    k: number of elements to be taken from pool

    This method uses mutlplicative formula'''
    # with scipy special.{combination, binomial coeff} returns 0 instead.
    if k < 0 or k > n: #try except maybe?
        return 0

    if k in [0,n]:
        return 1

    all_poss = 1 #minimum of comb
    for i in range(min(k, n - k)):
        all_poss = all_poss * (n - i) // (i + 1)

    return all_poss

from fractions import Fraction
def bernoulli_mult_NOTeffective(n): #! 1 - ... - comb(n,(n-1)) * Bn-1 * (n-(n-1)+1)^-1
    """Use multiplicative formula for binomial coefficient and a simplified form of taylor series???
    
    computation made with recursive definition for positives"""
    
    B = [1,(1/2)]
    if n == 0:
        return 1
    Sub = [1]
    #while len(B) != n:
        
    for k in range(n):
        if k+1 > len(B):
            B.append(bernoulli_mult_NOTeffective(k))
        #print(str(B)+ " THIS IS B")
        res = binomial(n,k) * (B[k]) * ((n-k+1)**-1)
        Sub.append(res)
        #print(str(Sub) + "dsads" + str(k))
    final = reduce(lambda x, y: x - y, Sub)
    Sub.clear()
    return final

#-----------------------------------------
#! PARTIAL FUNCTOOLS
# from functools import partial

# print(p(8))

#! https://scipy-lectures.org/packages/sympy.html#linear-algebra