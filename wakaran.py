import matplotlib.pyplot as plt
import numpy as np


N=1024
pp = np.linspace( 0, 4, N)   
def a(x):
     if x<=1: return 1/4.0
     if 1<=x and x<=2: return (3/8)*x-1/8.0
     if 2<=x and x<=3: return x/4+1/8
     if 3<=x: return -x/8+5/4.0

def p(x):
     if x<=1: return 1/4
     if 1<=x and x<=2: return 2/(11-3*x)
     if 2<=x and x<=3: return (4-x)/(13-4*x)
     if 3<=x: return 1

def r(x):
     if x<=1: return 1
     if 1<=x and x<=2: return 1
     if 2<=x : return (4-x)/2.0
     

def f(x):
     if x<=1: return 2/5
     if 1<=x and x<=2: return 4/(13-3*x)
     if 2<=x and x<=3: return (8-2*x)/(15-4*x)
     if 3<=x: return (8-2*x)/(6-x)

plt.plot(pp,[a(pp[k]) for k in range(N)],color='red',label='Acc')
plt.plot(pp,[p(pp[k]) for k in range(N)],color='green',label='Pre')
plt.plot(pp,[r(pp[k]) for k in range(N)],color='orange',label='Rec')
plt.plot(pp,[f(pp[k]) for k in range(N)],color='blue',label='F1')
plt.legend()
plt.show()
