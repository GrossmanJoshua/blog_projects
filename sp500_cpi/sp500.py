import numpy as np
from matplotlib.pyplot import *
import pickle

def get_rate(nyears, cpi_data, sp500):
  growth = {}
  cpi_cur = cpi_data[2016]
  for st in range(1913,2017-nyears):
    total_inv = 0.0
    current_val = 0.0
    for i in range(st,st+nyears):
      cpi = cpi_data[i]
      total_inv += cpi
      current_val = (current_val * (sp500[i]/sp500[i-1])) + cpi
    growth[st] = (total_inv/cpi_cur, current_val/cpi_cur)
  
  growth_rate = {i+nyears: (np.exp(np.log(j[1]/j[0])/nyears)-1)*100. for i,j in growth.items()}
  rates = [ (i,j) for i,j in sorted(growth_rate.items())]
  year,rate = zip(*rates)
  return year,rate

def load_data():
  with open('sp500_cpi.pkl','rb') as f:
    a,b = pickle.load(f)
  return a,b


def plot_data(a,b,constrate=.05):
  clf()
  const = {i+1910:(1+constrate)**i for i in range(120)}

  for i in range(10,41,10):
      x,y = get_rate(i,a,b)
      _,z = get_rate(i,a,const)
      lines = plot(x,((1+np.array(y)/100.)**i) / ((1+np.array(z)/100.)**i),'-',linewidth=i//20+1,ms=10,alpha=1)
      #x,y = get_rate(i,a,perc3)
      #plot(x,(1+np.array(y)/100.)**i,'--',alpha=0.75,color=lines[0].get_color())
  xlim([1923,2016])
  

