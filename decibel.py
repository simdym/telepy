import numpy as np

def from_dB(dB):
    return 10 ** (dB / 10)

def from_dBm(dBm):
    return 10 ** (dBm / 10) / 1000

def to_dB(gain):
    return 10 * np.log10(gain)

def to_dBm(V):
    return 10 * np.log10(V * 1000)