import numpy as np
import random

g = [1.3, 1.7, 1.0, 2.0, 1.3, 1.7, 2.0, 2.3, 2.0, 1.7, 1.3, 1.0, 2.0, 1.7, 1.7, 1.3, 2.0]

#TODO: Compute Mean and Variance using numpy and your own implementation and compare
#numpy
np_mean = np.mean(g)
np_var = np.var(g)


def vanila_mean(g):
    return sum(g) / len(g)

def vanila_var(g):
    g_mean = vanila_mean(g)
    dev = [(x - g_mean) ** 2 for x in g]
    return sum(dev) / len(g)




print("Numpy Mean and Var:")
print(np_mean, np_var)

print("Custom Mean and Var:")
print(vanila_mean(g), vanila_var(g))

