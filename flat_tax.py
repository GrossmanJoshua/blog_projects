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

def compute_rate(current_income_tax_income, total_income, npeople, offset):
      b = -total_income
      a = npeople * offset
      c = current_income_tax_income
      R = (-b - np.sqrt(b*b - 4*a*c))/(2 * a)
      return R,offset

# http://www.usgovernmentrevenue.com/current_revenue
# https://www.statista.com/statistics/216756/us-personal-income/
R,C = compute_rate(2.6e12, 15e12, 200e6, i, 25000)

incxs = np.logspace(3,np.log10(5000000),1000)
amnts = A([taxamount(i) for i in incxs])

# https://www.cbo.gov/sites/default/files/114th-congress-2015-2016/reports/51361-FigureData.xlsx
x = 1000.*A([8.3,32.6,58.6,94.9,140.3,195.5,259.9,321.5,1570.8]); y = A([3.3,8.4,12.8,17.0,20.7,23.0,26.3,26.3,34.0])/100.


clf(); plot(incxs,amnts); plot(incxs, np.clip(np.polyval([R,-C*R],incxs), 0, float('inf'))); xlim(0,500e3), ylim(0,200e3)
