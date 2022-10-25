import numpy as np
import matplotlib.pyplot as plt
import math
import winsound


def DigitsFixed(num, digits):
    return f"{num:.{digits}f}"


def is_correct_date(x, i):
    if i == 0:
        return x >= 0 and x <= 2.45
    elif i == 1:
        return x >= 0


winsound.Beep(2000,500)
print('(\t)'*3, 'Газодинамические функции v.0.0.1', '(\t)'*3, '\n', '*'*80)
while True:
    i = int(input('M -- 1, λ -- 0 '))
    if i == 0 or i == 1:
        while True:
            k = float(input('\nk = '))
            if k > 1:
                break
        while True:
            if i == 1:
                while True:
                    l = float(input('\nM = '))
                    if is_correct_date(l,i) == True:
                        f = pow((k+1)*(l**2)/(2+(l**2)*(k-1)), 1/2)
                        print('\nМах был преобразован в λ(', l,',', k, ') = ', f)
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
tl = 1.0-pow(f,2)*(k-1.0)/(k+1.0)
pl = pow(1-pow(f, 2)*(k-1)/(k+1), k/(k-1))
el = pow(1-(k-1)/(k+1)*pow(f, 2), 1/(k-1))
ql = f*pow((k+1)/2, 1/(k-1))*pow(1-pow(f, 2)*(k-1)/(k+1), 1/(k-1))
print('\nτ(λ) = ', DigitsFixed(tl, 6), 'π(λ) = ', DigitsFixed(pl, 6), 'ε(λ) = ', DigitsFixed(el, 6), 'q(λ) = ', DigitsFixed(ql, 6))



#x = np.arange(-10, 10.01, 0.01)
#plt.plot(x, x**2)
#plt.show()
