import eel # pip install eel
import math #pip install math но вроде стандарт уже не помню

eel.init("web")

def DigitsFixed(num, digits):
    return f"{num:.{digits}f}"


def check_data(f, check):
    if check == False:
        return f >= 0 and f <= 2.45
    else:
        return f >= 0

@eel.expose
def recv_data(vol, adiabatic, switching):
    k = float(adiabatic)
    val = float(vol)
    if k > 1 and k <= 1.67:
        if check_data(val, switching) == True:
            if switching == True:
                M = val
                f = pow((k+1)*(M**2)/(2+(M**2)*(k-1)), 1/2)
            else:
                f = val
                M = pow(2/(k+1)*(val**2)/(1-(val**2)*(k-1)/(k+1)), 1/2)

            tl = 1.0-pow(f,2)*(k-1.0)/(k+1.0)
            pl = pow(1-pow(f, 2)*(k-1)/(k+1), k/(k-1))
            el = pow(1-(k-1)/(k+1)*pow(f, 2), 1/(k-1))
            ql = f*pow((k+1)/2, 1/(k-1))*pow(1-pow(f, 2)*(k-1)/(k+1), 1/(k-1))
            resdata = 'λ = ' + str(DigitsFixed(f, 6)) + ' τ(λ) = ' + str(DigitsFixed(tl, 6)) + ' π(λ) = ' + str(DigitsFixed(pl, 6)) + ' ε(λ) = ' + str(DigitsFixed(el, 6)) + ' <br>q(λ) = ' + str(DigitsFixed(ql, 6)) + ' M = ' + str(DigitsFixed(M, 6))
            return resdata
        else:
            return "Значение не корректно"
    else:
        return "Значение коэффициента не корректно"







eel.start("index.html", size=(500, 700))
