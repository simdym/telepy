from abc import abstractmethod
import decibel as db
import numpy as np
from scipy.special import erf, erfc, erfinv, erfcinv

class FadingModel:
    def __init__(self):
        pass

    @abstractmethod
    def P_b(self, sinr):
        pass

class GaussianChannel(FadingModel):
    def P_b(self, sinr):
        return 1/2 * erfc(np.sqrt(sinr / 2))

    def sinr(self, P_b):
        return 2 * np.power(erfcinv(2 * P_b), 2)

class RayleighChannel(FadingModel):
    def P_b(self, sinr):
        return 1/2 * (1 - 1/(np.sqrt(1 + 2/sinr)))

    def sinr(self, P_b):
        return 2 / (1/np.power(1 - 2 * P_b, 2) - 1)

