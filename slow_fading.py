from abc import ABC, abstractmethod
import numpy as np

class ShadowingModel:
    def __init__(self, shadowing_std, **kwargs):
        self.shadowing_std = shadowing_std

    def prob_threshhold_signal(self):
        pass #yet to me implemented