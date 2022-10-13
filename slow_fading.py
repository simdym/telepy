from abc import ABC, abstractmethod
import numpy as np
from scipy.special import erf, erfc, erfinv, erfcinv

class ShadowingModel:
    def __init__(self, shadowing_std_db, **kwargs):
        self.shadowing_std_db = shadowing_std_db
        self.__dict__.update(kwargs)

    def prob_threshhold_signal(self, P_r_dbm, P_s_dbm):
        return 1/2 + 1/2 * erf((P_r_dbm - P_s_dbm)/np.sqrt(2) * self.shadowing_std_db)
