import numpy as np
from scipy.stats import beta
from matplotlib.pyplot import *

#TODO function to compute relative error
def get_rel_err(approx, ref):
    return None

#TODO standard monte carlo samplig
def std_mcs(func, n_samples):
    return None

#TODO control variate with control variates; we assume that we know the integral 'integral_cv_eval' of the control variate
def control_variate(func, cv, integral_cv_eval, n_samples):      
    return None

#TODO importance sampling using a beta distribution
def importance_sampling(func, a, b, n_samples):
    # generate samples from the beta distribution
    # ration between f and g_X
    return None

if __name__ == '__main__':
    # declare function to integrate via Monte Carlo sampling
    func = lambda x: np.exp(x)

    #TODO compute integral_0^1 func(x)dx
    integral_0_1 = None
    

    # declare vector with number of samples
    N = [1000, 10000, 100000, 1000000]

    # declare the control variates
    cv              = [lambda x: x, lambda x: 1. + x]
    
    #TODO compute their integral
    integral_cv     = None

    # declare values for the a and b parameters for the beta distributions
    a = [5, 0.5]
    b = [1, 0.5]

    # vector to put all relative errors
    rel_err_mcs   = np.zeros(len(N))
    rel_err_cv    = np.zeros((len(N), len(integral_cv)))
    rel_err_ip    = np.zeros((len(N), len(a)))

    #TODO for each N, perform Monte Carlo integration
    for i in range(len(N)):
        #TODO compute the relative error for the standard Monte Carlo sampling
        rel_err_mcs[i] = None

        #TODO compute the relative error for the control variate
        rel_err_cv[i] = None

        #TODO compute the relative error for the importance sampling
        rel_err_ip[i] = None

    #TODO plot results
    plot(N, rel_err_mcs, 'r-', label='Standard Monte Carlo')
    plot(N, rel_err_cv, 'b-', label='Control variate')
    plot(N, rel_err_ip, 'g-', label='Importance sampling')
    legend(loc='best')
    xlabel('Number of samples')
    ylabel('Relative error')
    title('Relative error of Monte Carlo integration')
    show()
    
