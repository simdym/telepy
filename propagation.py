from abc import ABC, abstractmethod
import numpy as np

class Channel:
    def __init__(self, P_T, G_T, G_R, **kwargs):
        self.P_T = P_T
        self.G_T = G_T
        self.G_R = G_R

    def P_R(self, distance):
        return self.P_T*self.G_T*self.G_R/self.propagation_loss(distance)

    @abstractmethod
    def propagation_loss(self, distance):
        pass


class FreeSpaceChannel(Channel):
    def __init__(self, P_T, G_T, G_R, wavelength):
        super().__init__(P_T, G_T, G_R)
        self.wavelength = wavelength

    def propagation_loss(self, distance):
        return np.power(4*np.pi*distance/self.wavelength)


class FlatTerrainChannel(Channel):
    def __init__(self, P_T, G_T, G_R, H_T, H_R):
        super().__init__(P_T, G_T, G_R)
        self.H_T = H_T
        self.H_R = H_R

    def propagation_loss(self, distance):
        return np.power(distance, 4)/np.power(self.H_T * self.H_R, 2)

