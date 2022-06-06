from scipy.interpolate import BPoly
import numpy as np
import matplotlib.pyplot as plt
# punkty kontrolne
#litera J
control_points = np.array([
    (0, 0), (1.2, -0.5), (1, 2), (1, 2)
])
#litera Z
control_points2 = np.array([
    (3, 2), (7, 2), (1, 0), (5, 0)
])

#utworzenie krzywej dla J
curve = BPoly(control_points[:, np.newaxis, :], [0, 1])
X = np.linspace(0, 1, 20)
sampled_points = curve(X)

#utworzenie krzywej dla Z
curve = BPoly(control_points2[:, np.newaxis, :], [0, 1])
X = np.linspace(0, 1, 20)
sampled_points2 = curve(X)

#generowanie wykresu
plt.gca().set_aspect('equal')
plt.plot(*sampled_points.T, '.-')
plt.plot(*sampled_points2.T, '.-')
#linie i punkty kontrolne
# plt.plot(*control_points.T, '-o')
# plt.plot(*control_points2.T, '-o')
plt.show()