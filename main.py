import numpy as np
import matplotlib.pyplot as plt
import math

k = 1.5
def is_correct_date(x, i):
    if i == 0:
        return x >= 0 and x <= 2.45
    elif i == 1:
        return x >= 0
while True:
    i = int(input('M -- 1, lambda -- 0 '))
    if i == 0 or i == 1:
        while True:
            k = float(input('k = '))
            if k > 1:
                break
        while True:
            if i == 1:
                while True:
                    l = float(input('\nM = '))
                    if is_correct_date(l,i) == True:
                        f = pow((k+1)*(l**2)/(2+(l**2)*(k-1)), 1/2)
                        print('\nМах был преобразован в лямбду l(', l,',', k, ') = ', f)
                        break
                break
            else:
                while True:
                    l = float(input('\nl = '))
                    if is_correct_date(l,i) == True:
                        f = l
                        break
                break
        break
    print('\nincorrect\n')
print('jopa')



#x = np.arange(-10, 10.01, 0.01)
#plt.plot(x, x**2)
#plt.show()
