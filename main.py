import eel # pip install eel
import math #pip install math но вроде стандарт уже не помню

eel.init("web")

def DigitsFixed(num, digits):
    return f"{num:.{digits}f}"

@eel.expose
def recv_data(val, adiabatic):
    f = float(val)
    k = float(adiabatic)
    tl = 1.0-pow(f,2)*(k-1.0)/(k+1.0)
    pl = pow(1-pow(f, 2)*(k-1)/(k+1), k/(k-1))
    el = pow(1-(k-1)/(k+1)*pow(f, 2), 1/(k-1))
    ql = f*pow((k+1)/2, 1/(k-1))*pow(1-pow(f, 2)*(k-1)/(k+1), 1/(k-1))
    return 'τ(λ) = ', DigitsFixed(tl, 6), ' π(λ) = ', DigitsFixed(pl, 6), ' ε(λ) = ', DigitsFixed(el, 6), ' q(λ) = ', DigitsFixed(ql, 6)


eel.start("index.html", size=(500, 700))
