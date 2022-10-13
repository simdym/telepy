import numpy as np
from scipy.constants import Boltzmann


def P_N(F, B, T_a=290):
    k = Boltzmann
    T_0 = 290
    return k * (T_a + T_0 * (F - 1)) * B
