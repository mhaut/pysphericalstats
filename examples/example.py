import pysphericalstats.fileIO as pySpfileIO
import pysphericalstats.convert as pySpCconvert
import pysphericalstats.math as pySpMath
import pysphericalstats.draw as pySpDraw
import matplotlib.pyplot as plt
import numpy as np

def main():
    #pathfile = "../datasets/XYZcoor.txt"
    pathfile = "../datasets/3dMDE.txt"
    vectorsMatrix = pySpfileIO.read_file(pathfile)
    
    
    dat         = pySpfileIO.load_data(vectorsMatrix)
    modules     = dat[:,0]
    coordinates = dat[:,3:6]


    print(coordinates.shape)
    exit()
    resultado = pySpMath.allmodulestatistics(modules)
    result    = pySpMath.allanglesstatistics(modules, coordinates)

    print(resultado)
    print(result)

    pySpDraw.draw_module_angle_distrib(dat)
    plt.show()
    pySpDraw.draw_density_graph(dat, save_image=False)
    plt.show()
    pySpDraw.draw_vector_graph(dat, save_image=True)
    #pySpDraw.draw_vector_graph(dat, save_image=False)
    #plt.show()



if __name__ == '__main__':
    main()
