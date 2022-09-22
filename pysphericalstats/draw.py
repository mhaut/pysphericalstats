import numpy as np
import pysphericalstats.convert as pySpCconvert
import pysphericalstats.math as pySpMath
import pysphericalstats.fileIO as pySpFileIO
import matplotlib.pyplot as plt
from scipy import stats
import os
from mpl_toolkits.mplot3d import Axes3D

DPIEXPORT = 81
plt.style.use('default')
#plt.style.use('ggplot')


def export_image(fig):
    path = pySpFileIO.get_output_path_file()
    if path != "":
        if not os.path.exists(path):
            os.makedirs(path)
        fig.savefig(path + "/moduleAngleGraph.svg")


def calculate_margin_max_coordinates(x, y, z, increment=2):
    return np.max(np.abs([x,y,z])) * increment


def draw_sphere(max_coordinates, alpha, line_width, ax):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x_sphere = max_coordinates * np.outer(np.cos(u), np.sin(v))
    y_sphere = max_coordinates * np.outer(np.sin(u), np.sin(v))
    z_sphere = max_coordinates * np.outer(np.ones(np.size(u)), np.cos(v))
    #ax.plot_surface(x_sphere,
                    #y_sphere,
                    #z_sphere,
                    #rstride=4,
                    #cstride=4,
                    #color='none',
                    #linewidth=line_width,
                    #alpha=alpha)
    # draw sphere
    u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
    #x = np.cos(u) * np.sin(v)
    #y = np.sin(u) * np.sin(v)
    #z = np.cos(v)
    ax.plot_wireframe(x_sphere, y_sphere, z_sphere, color="b", alpha=alpha)
    return ax.get_figure()


def draw_axis_vectors(margin, head_ratio, ax):
    soa = np.array([[0, 0, 0, margin, 0, 0], [0, 0, 0, 0, margin, 0],
                    [0, 0, 0, 0, 0, margin]])

    OX, OY, OZ, OU, OV, OW = zip(*soa)
    #ax.set_aspect('equal')
    ax.quiver(OX, OY, OZ, OU, OV, OW, arrow_length_ratio=head_ratio, color="k")
    ax.text(margin, 0, 1, "X", color='red')
    ax.text(0, margin, 1, "Y", color='red')
    ax.text(1, 0, margin, "Z", color='red')
    return ax.get_figure()


def draw_density_graph(dat, save_image=False):
    fig = plt.figure(dpi=DPIEXPORT, constrained_layout=True)
    fig.tight_layout(rect=[0.1,0.1,0.9, 0.95])
    ax = fig.add_subplot(111, projection='3d')
    
    # calculate density fields
    mu, sigma = 0, 0.1
    x = np.array([row[3] for row in dat])
    y = np.array([row[4] for row in dat])
    z = np.array([row[5] for row in dat])

    xyz = np.vstack([x, y, z])
    density = stats.gaussian_kde(xyz)(xyz)

    idx = density.argsort()
    x, y, z, density = x[idx], y[idx], z[idx], density[idx]

    # margins
    margin = calculate_margin_max_coordinates(x, y, z)

    # sphere
    draw_sphere(margin, 0.08, 0, ax)
    draw_axis_vectors(margin, 0.1, ax)

    # draw density fields
    ax.scatter(x, y, z, c=density)

    ax.set_xlim(margin * -1, margin)
    ax.set_ylim(margin * -1, margin)
    ax.set_zlim(margin * -1, margin)

    #manager = plt.get_current_fig_manager()
    #manager.window.showMaximized()
    plt.axis('off')
    plt.margins(0,0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    #fig.subplots_adjust(bottom=bottom_pos, top=top_pos, left=left_pos, right=right_pos)
    fig.tight_layout()
    if save_image: export_image(fig)
    return ax.get_figure()



def draw_module_angle_distrib(dat, save_image=False):
    module = dat[:,0]
    x, y, z = (*dat[:,3:6].T, )

    r = np.math.sqrt(np.sum(x) ** 2 + np.sum(y) ** 2 + np.sum(z) ** 2)
    meanX = np.sum(x) / r

    meanModule    = np.average(module)
    meanDirection = pySpMath.mean_direction((np.array([x, y, z]).T))

    if meanDirection[0] < 0: meanDirection[0] += 180
    if meanX < 0:            meanDirection[1] += 180
    if meanDirection[1] < 0: meanDirection[1] += 360

    Ax = meanModule * np.math.sin(pySpCconvert.to_radian(meanDirection[0])) * \
            np.math.cos(pySpCconvert.to_radian(meanDirection[1]))
    Ay = meanModule * np.math.sin(pySpCconvert.to_radian(meanDirection[0])) * \
            np.math.sin(pySpCconvert.to_radian(meanDirection[1]))
    Az = meanModule * np.math.cos(pySpCconvert.to_radian(meanDirection[0]))

    fig = plt.figure(dpi=DPIEXPORT, constrained_layout=True)
    fig.tight_layout(rect=[0.1,0.1,0.9, 0.95])
    ax = fig.add_subplot(111, projection='3d')

    max_absolute = np.max(np.abs(dat[:,3:6]))
    draw_sphere(max_absolute*1.25, 0.08, 0, ax)
    draw_axis_vectors(max_absolute*1.25, 0.05, ax)

    ax.quiver(0, 0, 0, x, y, z, arrow_length_ratio=0.01, linewidths=0.422)
    ax.quiver(0, 0, 0, Ax, Ay, Az, arrow_length_ratio=0.01, linewidths=0.844, color='r')
    #ax.set_xlim(np.array([max_absolute*-1, max_absolute])*0.5)
    #ax.set_ylim(np.array([max_absolute*-1, max_absolute])*0.5)
    #ax.set_zlim(np.array([max_absolute*-1, max_absolute])*0.5)
    ax.set_xlim(max_absolute*-1, max_absolute)
    ax.set_ylim(max_absolute*-1, max_absolute)
    ax.set_zlim(max_absolute*-1, max_absolute)
    plt.axis('off')
    if save_image: export_image(fig)
    return ax.get_figure()




def draw_vector_graph(dat, save_image=False):
    module = dat[:,0]
    x, y, z, x1, y1, z1 = (*dat[:,6:12].T, )

    r = np.math.sqrt(np.sum(x) ** 2 + np.sum(y) ** 2 + np.sum(z) ** 2)
    meanX = np.sum(x) / r

    meanModule    = np.average(module)
    meanDirection = pySpMath.mean_direction(np.array([x, y, z]).T)

    if meanDirection[0] < 0:   meanDirection[0] += 180
    if meanX < 0:              meanDirection[1] += 180
    if meanDirection[1] < 0:   meanDirection[1] += 360

    Ax = meanModule * np.math.sin(pySpCconvert.to_radian(meanDirection[0])) * \
            np.math.cos(pySpCconvert.to_radian(meanDirection[1]))

    Ay = meanModule * np.math.sin(pySpCconvert.to_radian(meanDirection[0])) * \
            np.math.sin(pySpCconvert.to_radian(meanDirection[1]))

    Az = meanModule * np.math.cos(pySpCconvert.to_radian(meanDirection[0]))
    # define 3d plot
    fig = plt.figure(dpi=DPIEXPORT, constrained_layout=True)
    fig.tight_layout(rect=[0.1,0.1,0.9, 0.95])
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(x, y, z, x1, y1, z1, arrow_length_ratio=0.01, linewidths=0.422)
    max_absolute = np.max(np.abs(dat[:,6:12]))
    min_value    = np.min(np.abs(dat[:,6:12]))
    ax.set_xlim(min_value, max_absolute)
    ax.set_ylim(min_value, max_absolute)
    ax.set_zlim(min_value, max_absolute)
    #plt.axis('off')
    if save_image: export_image(fig)
    return ax.get_figure()
