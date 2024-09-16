import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
from ZOA import OriginalZOA
from plot_res import *
#from data import *
def full_analysis():

    def fitness_function(solution):
        return np.sum(solution ** 2)

    problem_dict1 = {
        "fit_func": fitness_function,
        "lb": [-10, -15, -4, -2, -8],
        "ub": [10, 15, 12, 8, 20],
        "minmax": "min",
    }
    epoch = 50
    pop_size = 5000
    model = OriginalZOA(epoch, pop_size)
    best_position, best_fitness = model.solve(problem_dict1)

a =1
if a ==1:
    full_analysis()

DSR()