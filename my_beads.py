import numpy as np
import pyvista as pv
import matplotlib.pyplot as plt

np.set_printoptions(precision=3)

file = '.\\Data\\beads2d.vti'
mesh = pv.read(file)
plotter = pv.Plotter()

print(mesh.data_points)