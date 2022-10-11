from abc import ABC, abstractmethod
import numpy as np

class PropagationModel:
    def __init__(self, P_T, G_T, G_R, **kwargs):
        self.P_T = P_T
        self.G_T = G_T
        self.G_R = G_R

        if("shadowing_std" in kwargs):
            self.sigma = kwargs["shadowing_std"]
        if("")

    def P_R(self, distance):
        return self.P_T*self.G_T*self.G_R/self.propagation_loss(distance)

    @abstractmethod
    def propagation_loss(self, distance):
        pass


class FreeSpaceModel(PropagationModel):
    def __init__(self, P_T, G_T, G_R, wavelength):
        super().__init__(P_T, G_T, G_R)
        self.wavelength = wavelength

    def propagation_loss(self, distance):
        return np.power(4*np.pi*distance/self.wavelength)


class FlatTerrainModel(PropagationModel):
    def __init__(self, P_T, G_T, G_R, H_T, H_R):
        super().__init__(P_T, G_T, G_R)
        self.H_T = H_T
        self.H_R = H_R

    def propagation_loss(self, distance):
        return np.power(distance, 4)/np.power(self.H_T * self.H_R, 2)

class OkumuraHataModel(FlatTerrainModel):
    def __init__(self, P_T, G_T, G_R, H_T, H_R, f):
        super().__init__(P_T, G_T, G_R, H_T, H_R)
        self.f = f

    def propagation_loss(self, distance):
        #Convert to km
        distance /= 1000

        if(self.f < 200000000): #<200MHz
            a = (1.1*np.log10(self.f/10**6) - 0.7) * self.H_R - (1.56 * np.log10(self.f/10**6) - 0.8)
        elif(self.f < 400000000): #<400Mhz
            a = 8.29 * np.power(np.log10(1.54 * self.H_R), 2) - 1.1
        else:
            a = 3.2 * np.power(np.log10(11.75 * self.H_R), 2) - 4.97

        return 69.55 + 26.16 * np.log10(self.f/10**6) - 13.82 * np.log10(self.H_T) - a + (44.9 - 6.55 * np.log10(self.H_T)) * np.log10(distance)