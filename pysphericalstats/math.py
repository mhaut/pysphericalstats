import numpy as np
import pysphericalstats.convert as pySpCconvert
from scipy import stats



def calculate_vector_module(x, y, z, x1, y1, z1):
    return np.math.sqrt((x - x1)**2 + (y - y1)**2 + (z-z1)**2)


def mean_direction(coordinates_matrix):
    sum_coor = np.sum(coordinates_matrix, axis=0)
    n_elements = sum_coor.size
    r = np.math.sqrt(np.sum(sum_coor**2))
    mean_x, mean_y, mean_z = (*sum_coor / r, )
    if   mean_y > 0 and mean_x > 0:  mean_longitude = np.math.atan(mean_y / mean_x)
    elif mean_y > 0 and mean_x < 0:  mean_longitude = np.math.atan(mean_y / mean_x) + np.math.pi
    elif mean_y < 0 and mean_x < 0:  mean_longitude = np.math.atan(mean_y / mean_x) + np.math.pi
    elif mean_y < 0 and mean_x > 0:  mean_longitude = np.math.atan(mean_y / mean_x) + 2 * np.math.pi
    else:                            mean_longitude = 0
    mean_longitude = pySpCconvert.to_sexagesimal_3d(mean_longitude)
    mean_colatitud = np.math.acos(mean_z)
    mean_colatitud = pySpCconvert.to_sexagesimal_3d(mean_colatitud)
    return [mean_longitude, mean_colatitud]


def mean_module(coordinates_matrix):
    x,y,z = (*coordinates_matrix.T,)
    mean_module_ = np.math.sqrt(np.sum(x)**2 + np.sum(y)**2 + np.sum(z)**2) / x.size
    return mean_module_


def real_mod_to_unit_mod(coordinates_matrix):
    n_elements = coordinates_matrix.shape[0]
    polar_values = pySpCconvert.vector_to_polar(coordinates_matrix)
    u_vector    = np.ones((3, n_elements))
    u_vector[1] = polar_values[1]
    u_vector[2] = polar_values[2]
    unit_incr = pySpCconvert.vectors_to_rectangular(u_vector).T
    return unit_incr


def concentration_parameter(coordinates_matrix):
    x,y,z = (*coordinates_matrix.T,)
    n_elements = x.size
    mean_module_ = mean_module(coordinates_matrix)
    parameter = (n_elements - 1) / (n_elements * (1 - mean_module_))
    return parameter


def allmodulestatistics(modules, ndig=2):
    n_elements   = modules.size
    min_value    = min(modules)
    max_value    = max(modules)
    range_value  = psRange(modules)
    module_sum_  = module_sum(modules)
    m_arithmetic = np.average(modules)
    s_error      = standard_error(modules)
    s_d_module   = np.std(modules)
    s_d_module_p = module_population_standard_deviation(modules)
    v_module     = np.var(modules)
    v_module_p   = module_population_variance(modules)
    cs           = skewness_module_coefficient(modules)
    ca           = kurtois_module_coefficient(modules)
    formatSpec = '.'+str(ndig)+'f'
    string =  ("  ---------------------------  "  + "\n")
    string += ("  LINEAR STATISTICS - MODULES  "  + "\n")
    string += ("  ---------------------------  "  + "\n")
    string += ("  NUMBER OF ELEMENTS = "           + str(format(round(n_elements,ndig),   formatSpec))+ "\n")
    string += ("  MIN VALUE = "                    + str(format(round(min_value,ndig),    formatSpec))+ "\n")
    string += ("  MAX VALUE = "                    + str(format(round(max_value,ndig),    formatSpec))+ "\n")
    string += ("  RANGE = "                        + str(format(round(range_value,ndig),  formatSpec))+ "\n")
    string += ("  ARITHMETIC MEAN = "              + str(format(round(m_arithmetic,ndig), formatSpec))+ "\n")
    string += ("  MEAN STANDARD ERROR = "          + str(format(round(s_error,ndig),      formatSpec))+ "\n")
    string += ("  STANDARD DEVIATION = "           + str(format(round(s_d_module,ndig),   formatSpec))+ "\n")
    string += ("  VARIANCE = "                     + str(format(round(v_module,ndig),     formatSpec))+ "\n")
    string += ("  POPULATION STANDARD DEVIATION = "+ str(format(round(s_d_module_p,ndig), formatSpec))+ "\n")
    string += ("  POPULATION VARIANCE = "          + str(format(round(v_module_p,ndig),   formatSpec))+ "\n")
    string += ("  SKEWNESS COEFFICIENT = "         + str(format(round(cs,ndig),           formatSpec))+ "\n")
    string += ("  KURTOSIS COEFFICIENT = "         + str(format(round(ca,ndig),           formatSpec))+ "\n")
    return string + "\n"


def allanglesstatistics(modules, coordinates, ndig=2):
    vm_direction   = mean_direction(coordinates)
    vm_module      = mean_module(coordinates)
    unit_incr      = real_mod_to_unit_mod(coordinates)
    um_direction   = mean_direction(unit_incr)
    um_module      = mean_module(unit_incr)
    conc_parameter = concentration_parameter(unit_incr)
    sphericalErr   = spherical_error(unit_incr)
    formatSpec = '.'+str(ndig)+'f'
    string =  ("  -------------------------------  "        + "\n")
    string += ("  SPHERICAL STATISTICS - ANGLES    "        + "\n")
    string += ("  -------------------------------  "        + "\n")
    string += ("  NUMBER OF ELEMENTS = "                     + str(format(round(len(modules),ndig),    formatSpec)) + "\n")
    string += ("                                   "        + "\n")
    string += ("  Statistics for real (non-unit) vectors  " + "\n")
    string += ("  --------------------------------------  " + "\n")
    string += ("  COLATITUDE = "                             + str(format(round(vm_direction[1],ndig), formatSpec)) + "\n")
    string += ("  LONGITUDE = "                              + str(format(round(vm_direction[0],ndig), formatSpec)) + "\n")
    string += ("  MEAN MODULE = "                            + str(format(round(vm_module,ndig),       formatSpec)) + "\n")
    string += ("                                 "          + "\n")
    string += ("  Statistics for unit vectors    "          + "\n")
    string += ("  -----------------------------  "          + "\n")
    string += ("  COLATITUDE = "                             + str(format(round(um_direction[1],ndig), formatSpec)) + "\n")
    string += ("  LONGITUDE = "                              + str(format(round(um_direction[0],ndig), formatSpec)) + "\n")
    string += ("  MEAN MODULE = "                            + str(format(round(um_module,ndig),       formatSpec)) + "\n")
    string += ("  CONCENTRATION PARAMETER = "                + str(format(round(conc_parameter,ndig),  formatSpec)) + "\n")
    string += ("  SPHERICAL STANDARD ERROR = "               + str(format(round(sphericalErr,ndig),    formatSpec)) + "\n")
    return string + "\n"



def spherical_error(coordinates_matrix):
    n_elements = coordinates_matrix.shape[0]
    if n_elements >= 25:
        sum_coor = np.sum(coordinates_matrix, axis=0)
        r = np.math.sqrt(np.sum(sum_coor**2))

        mean_x, mean_y, mean_z = (*sum_coor / r, )
        x = coordinates_matrix[:,0] * mean_x
        y = coordinates_matrix[:,1] * mean_y
        z = coordinates_matrix[:,2] * mean_z
        sum2 = (x + y + z) ** 2
        d = 1 - (1/n_elements * np.math.fsum(sum2))
        Mm = mean_module(coordinates_matrix)
        sigma = np.sqrt(abs(d / (n_elements * Mm * Mm)))
        ea = np.log(0.05) * -1
        Q = np.arcsin(sigma * np.sqrt(ea))
        Q = pySpCconvert.to_sexagesimal_3d(Q)
        return Q


def module_population_variance(dat):
    return sum(((dat - np.average(dat)) ** 2)) / dat.size


def module_population_standard_deviation(dat):
    return np.math.sqrt((np.math.fsum((dat - np.average(dat)) ** 2)) / dat.size)


def skewness_module_coefficient(dat):
    n = dat.size
    return (n / float(((n - 1) * (n - 2)))) * np.math.fsum(((dat - np.average(dat)) / np.std(dat)) ** 3)


def kurtois_module_coefficient(dat):
    n = dat.size
    a = (n * (n + 1)) / ((n - 1) * (n - 2) * (n - 3))
    b = sum(((dat - np.average(dat)) / np.std(dat)) ** 4)
    c = (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
    return (a * b) - c


def psRange(dat):
    element_range = max(dat) - min(dat)
    if element_range < 0:
        element_range = element_range * -1
    return element_range


def module_sum(dat):
    return np.math.fsum(dat)


def standard_error(dat):
    return stats.sem(dat)
