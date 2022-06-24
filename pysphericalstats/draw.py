import numpy as np
import pysphericalstats.convert as pySpCconvert
import pysphericalstats.math as pySpMath
import pysphericalstats.fileIO as pySpFileIO
import matplotlib.pyplot as plt
from scipy import stats
import os


DPIEXPORT = 81
plt.style.use('default')
#plt.style.use('ggplot')


def export_image(fig):
    path = pySpFileIO.get_output_path_file()
    if path != "":
        if not os.path.exists(path):
            os.makedirs(path)
        fig.savefig(path + "/moduleAngleGraph.svg")


def calculate_margin_max_coordinates(x, y, z):
    """ Will calculate max element from three integers vectors

    :param x: integer vector x
    :param y: integer vector y
    :param z: integer vector z
    :return: Double of max value found in three parameters

    """
    margin = max(pySpMath.find_max(abs(x)), pySpMath.find_max(abs(y)), pySpMath.find_max(abs(z)))
    margin = margin * 2
    return margin


def draw_sphere(max_coordinates, alpha, line_width, ax):
    """ Will draw a sphere which center is coordinate center

    :param max_coordinates: integer radius value
    :param alpha: float alpha value for sphere surface
    :param line_width: float line width
    :param ax: Axis object where sphere will be displayed
    """
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x_sphere = max_coordinates * np.outer(np.cos(u), np.sin(v))
    y_sphere = max_coordinates * np.outer(np.sin(u), np.sin(v))
    z_sphere = max_coordinates * np.outer(np.ones(np.size(u)), np.cos(v))
    # ax.plot_surface(x_sphere,
    #                 y_sphere,
    #                 z_sphere,
    #                 rstride=4,
    #                 cstride=4,
    #                 color='none',
    #                 linewidth=line_width,
    #                 alpha=alpha)

    # draw sphere
    u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
    x = np.cos(u) * np.sin(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(v)
    ax.plot_wireframe(x_sphere, y_sphere, z_sphere, color="b", alpha=alpha)
    return ax.get_figure()


def draw_axis_vectors(margin, head_ratio, ax):
    """ Will draw three vectors from coordinates origin to max z, x, y values

    :param margin: float max value for three vectos
    :param head_ratio: float head-arrow ratio value
    :param ax: Axis object where vectors will be displayed
    """
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
    if save_image:
        export_image(fig)
        #plt.show()
    plt.axis('off') # this rows the rectangular frame 
    ax.get_xaxis().set_visible(False) # this removes the ticks and numbers for x axis
    ax.get_yaxis().set_visible(False) # this removes the ticks and numbers for y axis
    return ax.get_figure()



def draw_module_angle_distrib(dat, save_image=False):
    module = np.array([row[0] for row in dat])
    x = np.array([row[3] for row in dat])
    y = np.array([row[4] for row in dat])
    z = np.array([row[5] for row in dat])

    coord_vectors = [x, y, z]

    R = np.math.sqrt((np.sum(x) * np.sum(x)) + (np.sum(y) * np.sum(y)) + (np.sum(z) * np.sum(z)))
    meanX = np.sum(x) / R
    meanY = np.sum(y) / R
    meanZ = np.sum(z) / R

    meanModule = pySpMath.arithmetic_mean(module)
    meanDirection = pySpMath.mean_direction(coord_vectors)

    if meanDirection[0] < 0:
        meanDirection[0] = meanDirection[0] + 180

    if meanX < 0:
        meanDirection[1] = meanDirection[1] + 180

    if meanDirection[1] < 0:
        meanDirection[1] = meanDirection[1] + 360

    Ax = meanModule * np.math.sin(pySpCconvert.to_radian(meanDirection[0])) * \
            np.math.cos(pySpCconvert.to_radian(meanDirection[1]))

    Ay = meanModule * np.math.sin(pySpCconvert.to_radian(meanDirection[0])) * \
            np.math.sin(pySpCconvert.to_radian(meanDirection[1]))

    Az = meanModule * np.math.cos(pySpCconvert.to_radian(meanDirection[0]))

    fig = plt.figure(dpi=DPIEXPORT, constrained_layout=True)
    fig.tight_layout(rect=[0.1,0.1,0.9, 0.95])
    ax = fig.add_subplot(111, projection='3d')

    max_x = max(abs(x))
    max_y = max(abs(y))
    max_z = max(abs(z))
    max_absolute = max(max_x, max_y, max_z)

    draw_sphere(max_absolute*1.25, 0.08, 0, ax)
    draw_axis_vectors(max_absolute*1.25, 0.05, ax)


    ax.quiver(0, 0, 0, x, y, z, arrow_length_ratio=0.01, linewidths=0.422)
    #ax.set_xlim(np.array([max_absolute*-1, max_absolute])*0.5)
    #ax.set_ylim(np.array([max_absolute*-1, max_absolute])*0.5)
    #ax.set_zlim(np.array([max_absolute*-1, max_absolute])*0.5)
    ax.set_xlim(max_absolute*-1, max_absolute)
    ax.set_ylim(max_absolute*-1, max_absolute)
    ax.set_zlim(max_absolute*-1, max_absolute)

    # fig, ax = plt.subplots(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')

    #manager = plt.get_current_fig_manager()
    #manager.window.showMaximized()
    plt.axis('off')

    if save_image:
        export_image(fig)
    return ax.get_figure()




def draw_vector_graph(dat, save_image=False):
    module = np.array([row[0] for row in dat])
    x = np.array([row[6] for row in dat])
    y = np.array([row[7] for row in dat])
    z = np.array([row[8] for row in dat])

    x1 = np.array([row[9] for row in dat])
    y1 = np.array([row[10] for row in dat])
    z1 = np.array([row[11] for row in dat])

    coord_vectors = [x, y, z]

    R = np.math.sqrt((np.sum(x) * np.sum(x)) + (np.sum(y) * np.sum(y)) + (np.sum(z) * np.sum(z)))

    meanX = np.sum(x) / R
    meanY = np.sum(y) / R
    meanZ = np.sum(z) / R

    meanModule = pySpMath.arithmetic_mean(module)
    meanDirection = pySpMath.mean_direction(coord_vectors)

    if meanDirection[0] < 0:
        meanDirection[0] = meanDirection[0] + 180

    if meanX < 0:
        meanDirection[1] = meanDirection[1] + 180

    if meanDirection[1] < 0:
        meanDirection[1] = meanDirection[1] + 360

    Ax = meanModule * np.math.sin(pySpCconvert.to_radian(meanDirection[0])) * \
            np.math.cos(pySpCconvert.to_radian(meanDirection[1]))

    Ay = meanModule * np.math.sin(pySpCconvert.to_radian(meanDirection[0])) * \
            np.math.sin(pySpCconvert.to_radian(meanDirection[1]))

    Az = meanModule * np.math.cos(pySpCconvert.to_radian(meanDirection[0]))


    # define 3d plot
    fig = plt.figure(dpi=DPIEXPORT, constrained_layout=True)
    fig.tight_layout(rect=[0.1,0.1,0.9, 0.95])
    ax = fig.add_subplot(111, projection='3d')

    max_x = max(abs(x))
    max_y = max(abs(y))
    max_z = max(abs(z))
    max_x1 = max(abs(x1))
    max_y1 = max(abs(y1))
    max_z1 = max(abs(z1))

    min_x = min(x)
    min_y = min(y)
    min_z = min(z)
    min_x1 = min(x1)
    min_y1 = min(y1)
    min_z1 = min(z1)

    max_absolute = max(max_x, max_y, max_z, max_x1, max_y1, max_z1)
    min_value = min(min_x, min_y, min_z, min_x1, min_y1, min_z1)

    ax.quiver(x, y, z, x1, y1, z1, arrow_length_ratio=0.01, linewidths=0.422)
    ax.set_xlim(min_value, max_absolute)
    ax.set_ylim(min_value, max_absolute)
    ax.set_zlim(min_value, max_absolute)


    if save_image:
        export_image(fig)

    return ax.get_figure()
