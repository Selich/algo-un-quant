import numpy as np
import chaospy as cp
from scipy.integrate import odeint
from matplotlib.pyplot import *

# to use the odeint function, we need to transform the second order differential equation
# into a system of two linear equations
def model(w, t, p):
	x1, x2 		= w
	c, k, f, w 	= p

	f = [x2, f*np.cos(w*t) - k*x1 - c*x2]

	return f

# discretize the oscillator using the odeint function
def discretize_oscillator_odeint(model, atol, rtol, init_cond, args, t, t_interest=None):
    sol = odeint(model, init_cond, t, args=(args,), atol=atol, rtol=rtol)

    if t_interest == None:
       return sol[:, 0]

    return sol[t_interest, 0]

if __name__ == '__main__':
    # relative and absolute tolerances for the ode int solver
    atol = 1e-10
    rtol = 1e-10

    # TODO: initiate deterministic parameters setup as specified in the assignement [c, k, f, y0, y1]
    c = 1.0
    k = 1.0
    f = 1.0
    y0 = 0.0
    y1 = 0.0

    # TODO: specify time domain setup
    t = np.linspace(0, 10, 100)

    # TODO: initial conditions and parameters setup
    init_cond = [y0, y1]
    args = [c, k, f]

    # TODO: w is no longer deterministic...
    w = 1.0

    # TODO: perform Monte Carlo sampling computations
    y_mc = np.random.uniform(0, np.pi, 100)

    # TODO: print results
    print("Deterministic solution:")
    print(discretize_oscillator_odeint(model, atol, rtol, init_cond, args, t))
    print("Monte Carlo solution:")
    print(y_mc)


