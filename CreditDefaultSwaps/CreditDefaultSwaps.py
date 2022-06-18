import numpy as np
import collections
import matplotlib.pyplot as plt
import scipy.interpolate
import scipy.optimize
import sympy
import pandas as pd

"""Решение"""

# доопределили нулем в момент времени 0
Germany = np.array([0, -0.455, 0.059, 0.241, 0.404, 0.536, 0.561, 0.578, 0.609, 0.646, 0.711]) / 100
Italy = np.array([0, -0.320, 0.501, 1.183, 1.464, 1.541, 1.819, 1.966, 2.221, 2.334, 2.385]) / 100
years = np.array([i for i in range(11)])

R = 0.4
D = np.array([(i+1)*(Italy[i] - Germany[i]) for i in range(11)])
D = D / (1 - R)
S = 1 - D # в момент времени 0 S(0) = 1
f = scipy.interpolate.interp1d(years, S, kind = 'linear')

tenors = [i*0.25 for i in range(1, 41)]
values = f(tenors)
total_pay = np.sum(values)
x = 4*(1-R)*(1-S[10])/total_pay
print('x =',x*100, '%')

"""Проверка"""

# доопределили нулем в момент времени 0
Germany = np.array([0, -0.455, 0.059, 0.241, 0.404, 0.536, 0.561, 0.578, 0.609, 0.646, 0.711]) / 100

# увеличим риски по Италии
Italy = np.array([0, -0.320, 0.501, 1.183, 1.464, 1.541, 1.819, 1.966, 2.221, 2.334, 2.385]) + 0.5
Italy /= 100
years = np.array([i for i in range(11)])

R = 0.4
D = np.array([(i+1)*(Italy[i] - Germany[i]) for i in range(11)])
D = D / (1 - R)
S = 1 - D # в момент времени 0 S(0) = 1
f = scipy.interpolate.interp1d(years, S, kind = 'linear')


tenors = [i*0.25 for i in range(1, 41)]
values = f(tenors)
total_pay = np.sum(values)
x = 4*(1-R)*(1-S[10])/total_pay
print('x =',x*100, '%')

