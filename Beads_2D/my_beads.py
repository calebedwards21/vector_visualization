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
# NOT WORKING
time = 0
sample = 8
x0 = xn[::sample, ::sample, :]
y0 = yn[::sample, ::sample, :]
u0 = un[::sample, ::sample, :]
v0 = vn[::sample, ::sample, :]
magnitude = mag[::sample, ::sample, :]
fig = plt.figure()
axis = plt.axes(xlim=(-2,2), ylim=(-2,2))
# Q = plt.quiver(x0[:,:,time], y0[:,:,time], u0[:,:,time], v0[:,:,time])
Q = plt.contourf(xn[:,:,time], yn[:,:,time], magnitude[:,:,time])
plt.colorbar()

def updateAnimation(frame):
    print(frame)
    Q.set_UVC(u0[:,:,frame], v0[:,:,frame])
    return Q

anim = FuncAnimation(fig, updateAnimation, frames=zn.shape[2], interval=10)
# plt.show()

anim.save('./Images/beads_contour.gif', fps=60)


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