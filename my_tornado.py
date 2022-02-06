import numpy as np
import pyvista as pv
import matplotlib.pyplot as plt

np.set_printoptions(precision=3)

file = '.\\Data\\tornado3d.vti'
mesh = pv.read(file)
plotter = pv.Plotter()


z = mesh.points[:, 0]
y = mesh.points[:, 1]
x = mesh.points[:, 2]
x.shape = y.shape = z.shape = 128, 128, 128

w,v,u = mesh.point_data['w'], mesh.point_data['v'], mesh.point_data['u']
# w.shape = v.shape = u.shape = mesh.dimensions
mag = (np.sqrt(u**2 + v**2 + w**2))

# 2D Slicing
# sample = 5
# slice = 64
# # plt.imshow(mag[:, :, 0])
# plt.contourf(x[:, :, slice],y[:, :, slice],mag[:, :, slice])
# plt.quiver(x[::sample, ::sample, slice],y[::sample, ::sample, slice],u[::sample, ::sample, slice], v[::sample, ::sample, slice])
# plt.colorbar()
# plt.axis('square')
# plt.show()

# ADD CAMERA
camera = pv.Camera()
plotter.camera.position = (15, 15, 15)
plotter.camera.focal_point = (0,0,0)
plotter.camera = camera


# POINT CLOUD
samp = 10
points = mesh.points
points = points[::samp]

vectors = np.vstack((w,v,u)).T
vectors = vectors[::samp]

point_cloud = pv.PolyData(points)
point_cloud['vectors'] = vectors
arrows = point_cloud.glyph(orient='vectors', scale=True, factor=0.15)
plotter.add_mesh(point_cloud, point_size=2.5, render_points_as_spheres=True, opacity=0.4)
# plotter.add_mesh(arrows)
plotter.show()


# VOLUME
# vol = 20*np.log10(np.sqrt(u**2 + v**2 + w**2))
# # mesh['points'] = np.sqrt(mesh.point_data['u']**2 + mesh.point_data['v']**2 + mesh.point_data['w']**2)
# plotter.add_volume(vol)


# PLOTTER


