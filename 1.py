import propagation as prop
import slow_fading as slow
import fast_fading as fast
import noise
import decibel as db

import matplotlib.pyplot as plt
import numpy as np

P_T = 1
G_T = db.from_dB(1)
G_R = db.from_dB(12)
H_T = 100
H_R = 1
F = db.from_dB(3)
B = 8*1000
f = 900 * 10**6

rayleigh = fast.RayleighChannel()

sinr = rayleigh.sinr(10**-3)
P_N = noise.P_N(F, B)
P_S = sinr*P_N

print("Noise", P_N, db.to_dBm(P_N))
print("SINR", sinr, db.to_dB(sinr))
print("P_S", P_S, db.to_dBm(P_S))

prop_model = prop.OkumuraHataModel(P_T, G_T, G_R, H_T, H_R, f)
shadowing_model = slow.ShadowingModel(8)

distance = np.linspace(100, 10**4, 10**4)
P_R = prop_model.P_R(distance)
P = shadowing_model.prob_threshhold_signal(db.to_dBm(P_R), db.to_dBm(P_S))

distance_min = distance[P > 0.9][-1]
L_min = prop_model.propagation_loss(distance_min)
P_R_min = prop_model.P_R(distance_min)

print("Min distance", distance_min)
print("P_R", P_R_min, db.to_dBm(P_R_min))
print("L", L_min, db.to_dB(L_min))

plt.plot([distance_min, distance_min], [0, 1])
plt.plot(distance, P)
plt.show()

M = 2
print("\nWith M=" + str(M))

sinr = rayleigh.sinr(10**-3, M=2)
P_S = sinr*P_N

P_R_min = prop_model.P_R(distance_min)
P_min = shadowing_model.prob_threshhold_signal(db.to_dBm(P_R_min), db.to_dBm(P_S))

print("Noise", P_N, db.to_dBm(P_N))
print("SINR", sinr, db.to_dB(sinr))
print("P_S", P_S, db.to_dBm(P_S))
print("L", L_min, db.to_dB(L_min))
print("P_R", P_R_min, db.to_dBm(P_R_min))
print("P", P_min)

P = shadowing_model.prob_threshhold_signal(db.to_dBm(P_R), db.to_dBm(P_S))
plt.plot([distance_min, distance_min], [0, 1])
plt.plot(distance, P)
plt.show()

