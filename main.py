import AGModels
import numpy as np
import matplotlib.pyplot as plt

def u(t, u0, t0, tE):
    return np.sqrt(u0**2+((t-t0)/tE)**2)

def A(u):
    return (u**2+2)/(u*np.sqrt(u**2+4))

def mlens(params,t):
    m0, u0, t0, tE, g = params
    return m0 - 2.5*np.log10(g*A(u(t, u0, t0, tE))+(1-g))

def sinu(params, t):
    A, w, phase = params
    return A*np.sin(w*t+phase)

def parab(params, t):
    A, B, C = params
    return A*(t-B)**2 + C

def gaussian(params, t):
    a,b,c = params
    return a*np.exp(-(t-b)**2) + c

def o():
    plt.gca().invert_yaxis()

guessparams = [15.0,0.1,8375,10,1]
AGModels.proto_fit_NL("KMTC15_I.pysis", mlens, guessparams, o)


params = (2, 3, 1)
guess_params = (3, 4, 0.5)
ps, uncs = AGModels.system_test(gaussian, params, 0, 6, guess_params)
print(ps)
