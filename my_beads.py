from tokenize import Double
import numpy as np
import pyvista as pv
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter, FuncAnimation


# np.set_printoptions(precision=5)

file = '.\\Data\\beads2d.vti'

mesh = pv.read(file)
print(mesh)

x = mesh.x.copy()
y = mesh.y.copy()
z = mesh.z.copy()

u = mesh.point_data['u']
v = mesh.point_data['v']

xn = np.reshape(x, mesh.dimensions, order='F')
yn = np.reshape(y, mesh.dimensions, order='F')
zn = np.reshape(z, mesh.dimensions, order='F')

un = np.reshape(u, mesh.dimensions, order='F')
vn = np.reshape(v, mesh.dimensions, order='F')

mag = np.sqrt(un**2 + vn**2)

# MATPLOTLIB GIF
fig = plt.figure()
axis = plt.axes(xlim=(-2,2), ylim=(-2,2))
Q = plt.contourf(xn[:,:,0], yn[:,:,0], mag[:,:,0])
plt.colorbar()

def AnimationFunction(frame):
    Q = plt.contourf(xn[:,:,frame], yn[:,:,frame], mag[:,:,frame])
    return Q

anim = FuncAnimation(fig, AnimationFunction, interval=zn.shape[2], blit=False)
anim.save('beads_mpl.gif', fps=30)
fig.tight_layout()
plt.show()


# PYVISTA GIF
# grid = pv.StructuredGrid(xn[:,:,0], yn[:,:,0], mag[:,:,0])
# plotter = pv.Plotter(notebook=False, off_screen=True)
# plotter.add_mesh(grid, scalars=zn[:,:,0].ravel(), clim=[0, 1])

# # Open a gif
# plotter.open_gif("beads.gif")
# plotter.camera_position = 'xy'
# pts = grid.points.copy()

# for i in range(zn.shape[2]): #[::20]: # 512
#     print(i)
#     pts[:, -1] = mag[:,:,i].ravel()
#     plotter.update_coordinates(pts, render=False)
#     plotter.update_scalars(mag[:,:,i].ravel(), render=False)
#     plotter.render()
#     plotter.write_frame()

# # Closes and finalizes movie
# plotter.close()    

# 2D Contour Plot - Matplotlib
# n = 64
# plt.contourf(xn[:,n,:], zn[:,n,:], mag[:,n,:])
# # plt.axis('square')
# plt.colorbar()
# plt.show()