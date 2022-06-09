import sys
#sys.path.append("C:\\Users\\josei\\Desktop\\pysphericalstats-main_ultimaVersionGit\\pysphericalstats-main\\pysphericalstats")
sys.path.append("/home/titan/software/pysphericalstats-main/pysphericalstats-main/pysphericalstats")

import pysphericalstats.fileIO as pySpfileIO
import pysphericalstats.convert as pySpCconvert
import pysphericalstats.math as pySpMath
import pysphericalstats.draw as pySpDraw
import matplotlib.pyplot as plt


def main():
    pathfile = "../dataset/XYZcoor.txt"
    vectorsMatrix = pySpfileIO.read_file(pathfile)
    
    
    dat     = pySpfileIO.load_data(vectorsMatrix)
    modules = pySpfileIO.getColumnAsArray(0, dat)

    resultado = pySpMath.allmodulestatistics(modules)
    print(resultado)

    coordinates = (
        pySpMath.getColumnAsArray(3, dat), pySpMath.getColumnAsArray(4, dat), pySpMath.getColumnAsArray(5, dat))

    result = pySpMath.allanglesstatistics(modules, coordinates)
    print(result)

    pySpDraw.draw_module_angle_distrib(dat)
    plt.show()
    pySpDraw.draw_density_graph(dat, save_image=False)
    plt.show()
    pySpDraw.draw_vector_graph(dat, save_image=True)
    plt.show()



if __name__ == '__main__':
    main()
