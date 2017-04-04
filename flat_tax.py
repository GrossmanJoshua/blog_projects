import numpy as np
from matplotlib.pyplot import *

A = np.array

def taxamount(inc):
     inc = inc - 6350
     if inc < 0:
         return 0
     tb = A([0,9325,37950,91900,191650,416700,418400])
     rate = A([10,15,25,28,33,35,39.6])/100.
     idx = np.nonzero(inc > tb)[0][-1]
     tot = sum((tb[i+1]-tb[i]) * rate[i] for i in range(idx))
     tot += (inc-tb[idx])*rate[idx]
     return tot

def compute_rate(current_income_tax_income, total_income, npeople, equalrate_dollars, equalrate_tax):
     return (current_income_tax_income - npeople*equalrate_tax) / (total_income - npeople * equalrate_dollars)

i = 191650
R = compute_rate(2.6e12, 15e12, 200e6, i, taxamount(i))
C = i-taxamount(i)/R

incxs = np.logspace(3,np.log10(5000000),1000)
amnts = A([taxamount(i) for i in incxs])

clf(); plot(incxs,amnts); plot(incxs, np.clip(np.polyval([R,-C*R],incxs), 0, float('inf'))); xlim(0,500e3), ylim(0,200e3)
