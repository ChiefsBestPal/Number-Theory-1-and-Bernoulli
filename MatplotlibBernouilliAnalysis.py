import numpy as np
import matplotlib
import pandas

## none

import time
import timeit
bernoulli_test = """
import sympy as sym
#from sympy import *
sym.init_printing(use_unicode=False, wrap_line=True)

def bernoulli_number(n):
    def pyramid(arr):
            #uses summation of n partial sum testing
        if len(arr) <= 1:
            return "not a pyramid"
        S,l =int(),0
        while len(arr) != S:
            l += 1
            S = (l/2)*(l+1)
        #print("layers: " + str(l),sep=" ")
        n = -1
        s0 = lambda n: (n/2)*(n+1)
        s1 = lambda n: ((n+1)/2)*((n+2))
        while n != l:
            n += 1
            a = arr[int(s0(n)):int(s1(n))]
            if a:
                yield a

    def pascals_bernoulli(n):
        Triangle = []
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
        res = sym.N(sym.solve(sum(temp),(x))[0])
        B.append(res)
        res = int()
        temp.clear()
    return B[n]
    #inital arr: list(pyramid(pascals_bernoulli(n+1)))

print("Proper bernoulli number solved with a variation of pascals pyramid (not recursive method with summation until n-1 and the binomial coefficient lol)",end=":  \\n ")
print(bernoulli_number(50),flush=False)
"""
#print(timeit.timeit(stmt=bernoulli_test,number=1),end=" ")
#quit()
import matplotlib.pyplot as plt
import numpy as np
# def same(*values): return (abs(i) for i in values for _ in range(5))
# y = list(it.chain(*list(map(lambda x: (same(x)),(0.0757575757575758,-2.83822495706962e+78,-1.98382953521301e+735,-5.31870446941632e+1769)))))
x = np.linspace(0.4, 15, 100)
y = np.linspace(0, 5.31870446941632e+1769, 100)
print("seconds <____> for this test")
arr1000 = [14.0571053,13.9828119,13.9919299,13.89999,14.0771525]#! -5.31870446941632e+1769
arr500 = [4.7344481,4.765309800000001,4.6504608,4.618301600000001,4.5989108]#!-1.98382953521301e+735
arr100 = [0.9971545,1.02998,0.9928838,1.0149545,1.0077063] #!-2.83822495706962e+78
arr10 = [0.4210303,0.456654,0.42810430000000005,0.4412566,0.4239719] #!0.0757575757575758
# x-axis values 
x = []
x.extend(arr10)
x.extend(arr100)
x.extend(arr500)
x.extend(arr1000)
import itertools as it
# Y-axis values
def same(*values): return (abs(i) for i in values for _ in range(5))
y = list(it.chain(*list(map(lambda x: (same(x)),(0.0757575757575758,-2.83822495706962e+78,-1.98382953521301e+735,-5.31870446941632e+1769)))))
print(x,y)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.4, 15, 100)
y = np.linspace(0, 5.31870446941632e+1769, 100)
print(x,y)
fig, ax = plt.subplots()
ax.plot(x, y)

exp = lambda x: 10**(x)
log = lambda x: np.log(x)

# Set y scale to exponential
ax.set_yscale('function', functions=(exp, log))
ax.set(xlim=(0.42,14.0771525), ylim=(0.0757575757575758,5.31870446941632e+1769))
ax.set_yticks([0.0757575757575758,2.83822495706962e+78,1.98382953521301e+735,5.31870446941632e+1769])

plt.show()
matplotlib.pyplot.scatter(x,y)
matplotlib.pyplot.show()
#! Warning: Axis at Nan or inf if B is too demanding... This is just personal alg tests

# import subprocess
# proc=subprocess.Popen("print timeit.timeit(globals=globals(),stmt=bernoulli_test,number=1,timer=time.perf_counter)", shell=True, stdout=subprocess.PIPE, )
# output=proc.communicate()[0]
# print(output)
