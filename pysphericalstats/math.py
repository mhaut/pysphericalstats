import numpy as np
import pysphericalstats.convert as pySpCconvert
from pysphericalstats.fileIO import getColumnAsArray
from scipy import stats

def find_max(numbers):
    max_element = numbers[0]
    for element in numbers:
        if element < 0:
            element = element * -1
        if element > max_element:
            max_element = element
    return max_element

def calculate_vector_module(x, y, z, x1, y1, z1):
    return np.math.sqrt(((x - x1)**2) + ((y - y1)**2) + ((z-z1)**2))

#Estas son de AngleStatisticsManager
def mean_direction(coordinates_matrix):
    x = coordinates_matrix[0]
    y = coordinates_matrix[1]
    z = coordinates_matrix[2]

    mean = []
    n_elements = len(x)
    r = np.math.sqrt((np.sum(x) * np.sum(x)) + (np.sum(y) * np.sum(y)) + (np.sum(z) * np.sum(z)))

    mean_x = np.sum(x) / r
    mean_y = np.sum(y) / r
    mean_z = np.sum(z) / r
    mean_longitude = 0

    if mean_y > 0 and mean_x > 0:
        mean_longitude = np.math.atan(mean_y / mean_x)

    if mean_y > 0 > mean_x:
        mean_longitude = np.math.atan(mean_y / mean_x) + np.math.pi

    if mean_y < 0 and mean_x < 0:
        mean_longitude = np.math.atan(mean_y / mean_x) + np.math.pi

    if mean_y < 0 < mean_x:
        mean_longitude = np.math.atan(mean_y / mean_x) + (2 * np.math.pi)

    mean_longitude = pySpCconvert.to_sexagesimal_3d(mean_longitude)
    mean_colatitud = np.math.acos(mean_z)
    mean_colatitud = pySpCconvert.to_sexagesimal_3d(mean_colatitud)

    mean.append(mean_longitude)
    mean.append(mean_colatitud)
    return mean

def mean_module(coordinates_matrix):
    x = coordinates_matrix[0]
    y = coordinates_matrix[1]
    z = coordinates_matrix[2]
    n_elements = len(x)
    r = np.math.sqrt((np.sum(x) * np.sum(x)) + (np.sum(y) * np.sum(y)) + (np.sum(z) * np.sum(z)))

    mean_module_ = r / n_elements

    return mean_module_

def real_mod_to_unit_mod(coordinates_matrix):
    x = coordinates_matrix[0]
    y = coordinates_matrix[1]
    z = coordinates_matrix[2]

    n_elements = len(x)

    polar_values = pySpCconvert.vector_to_polar(coordinates_matrix)
    module = [1] * n_elements
    colatitud = getColumnAsArray(1, polar_values)
    longitude = getColumnAsArray(2, polar_values)
    # colatitud = polar_values[:, 1]
    # longitude = polar_values[:, 2]

    u_vector = [module, colatitud, longitude]
    unit_incr = pySpCconvert.vectors_to_rectangular(u_vector)

    return unit_incr


def concentration_parameter(coordinates_matrix):
    x = coordinates_matrix[0]
    y = coordinates_matrix[1]
    z = coordinates_matrix[2]
    n_elements = len(x)
    mean_module_ = mean_module(coordinates_matrix)
    parameter = (n_elements - 1) / float((n_elements * (1 - mean_module_)))

    return parameter

def allmodulestatistics(modules, ndig=2):
    # estas en math.py
    n_elements = len(modules)
    min_value = min(modules)
    max_value = max(modules)
    range_value = psRange(modules)
    module_sum_ = module_sum(modules)
    m_arithmetic = arithmetic_mean(modules)
    s_error = standard_error(modules)
    s_d_module = module_standard_deviation(modules)
    s_d_module_p = module_population_standard_deviation(modules)
    v_module = module_variance(modules)
    v_module_p = module_population_variance(modules)
    cs = skewness_module_coefficient(modules)
    ca = kurtois_module_coefficient(modules)

    formatSpec = '.'+str(ndig)+'f'
    string = ("  ---------------------------  " + "\n")
    string += ("  LINEAR STATISTICS - MODULES  "+ "\n")
    string += ("  ---------------------------  "+ "\n")
    string += ("  NUMBER OF ELEMENTS            ="+ str(format(round(n_elements,ndig),formatSpec))+ "\n")
    string += ("  MIN VALUE                     ="+ str(format(round(min_value,ndig),formatSpec))+ "\n")
    string += ("  MAX VALUE                     ="+ str(format(round(max_value,ndig),formatSpec))+ "\n")
    string += ("  RANGE                         ="+ str(format(round(range_value,ndig),formatSpec))+ "\n")
    string += ("  ARITHMETIC MEAN               ="+ str(format(round(m_arithmetic,ndig),formatSpec))+ "\n")
    string += ("  MEAN STANDARD ERROR           ="+ str(format(round(s_error,ndig),formatSpec))+ "\n")
    string += ("  STANDARD DEVIATION            ="+ str(format(round(s_d_module,ndig),formatSpec))+ "\n")
    string += ("  VARIANCE                      ="+ str(format(round(v_module,ndig),formatSpec))+ "\n")
    string += ("  POPULATION STANDARD DEVIATION ="+ str(format(round(s_d_module,ndig),formatSpec))+ "\n")
    string += ("  POPULATION VARIANCE           ="+ str(format(round(v_module_p,ndig),formatSpec))+ "\n")
    string += ("  SKEWNESS COEFFICIENT          ="+ str(format(round(cs,ndig),formatSpec))+ "\n")
    string += ("  KURTOSIS COEFFICIENT          ="+ str(format(round(ca,ndig),formatSpec))+ "\n")

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
    string =  ("  -------------------------------  " + "\n")
    string += ("  SPHERICAL STATISTICS - ANGLES    " + "\n")
    string += ("  -------------------------------  " + "\n")
    string += ("  NUMBER OF ELEMENTS =" + str(format(round(len(modules),ndig),formatSpec)) + "\n")
    string += ("                                   " + "\n")
    string += ("  Statistics for real (non-unit) vectors  " + "\n")
    string += ("  --------------------------------------  " + "\n")
    string += ("  COLATITUDE  ="+ str(format(round(vm_direction[1],ndig),formatSpec)) + "\n")
    string += ("  LONGITUDE   ="+ str(format(round(vm_direction[0],ndig),formatSpec)) + "\n")
    string += ("  MEAN MODULE ="+ str(format(round(vm_module,ndig),formatSpec)) + "\n")
    string += ("                                 " + "\n")
    string += ("  Statistics for unit vectors    " + "\n")
    string += ("  -----------------------------  " + "\n")
    string += ("  COLATITUDE                ="+ str(format(round(um_direction[1],ndig),formatSpec)) + "\n")
    string += ("  LONGITUDE                 ="+ str(format(round(um_direction[0],ndig),formatSpec)) + "\n")
    string += ("  MEAN MODULE               ="+ str(format(round(um_module,ndig),formatSpec)) + "\n")
    string += ("  CONCENTRATION PARAMETER   ="+ str(format(round(conc_parameter,ndig),formatSpec)) + "\n")
    string += ("  SPHERICAL STANDARD ERROR  ="+ str(format(round(sphericalErr,ndig),formatSpec)) + "\n")

    return string + "\n"

def spherical_error(coordinates_matrix):
    x = coordinates_matrix[0]
    y = coordinates_matrix[1]
    z = coordinates_matrix[2]
    n_elements = len(x)

    if n_elements >= 25:
        r = np.math.sqrt((np.sum(x) * np.sum(x)) + (np.sum(y) * np.sum(y)) + (np.sum(z) * np.sum(z)))
        mean_x = np.sum(x) / float(r)
        mean_y = np.sum(y) / float(r)
        mean_z = np.sum(z) / float(r)
        x = x * mean_x
        y = y * mean_y
        z = z * mean_z
        sum = x + y + z
        sum2 = sum ** 2
        d = 1 - (1/float(n_elements) * np.math.fsum(sum2))
        Mm = mean_module(coordinates_matrix)
        sigma = np.sqrt(abs(d / float(n_elements * Mm * Mm)))
        ea = np.log(0.05) *-1
        Q = np.arcsin(sigma * np.sqrt(ea))
        Q = pySpCconvert.to_sexagesimal_3d(Q)

        return Q

#Estas son de ModuleStatisticsManager
def arithmetic_mean(data):
    return np.sum(data) / len(data)

def module_variance(dat):
    """ TEST SMALL ERROR
    """
    m_arit = arithmetic_mean(dat)
    n = len(dat)
    return np.math.fsum(((dat - m_arit) ** 2)) / (n - 1)

def module_standard_deviation(dat):
    """ TEST SMALL ERROR
            """
    m_arit = arithmetic_mean(dat)
    n = len(dat)
    return np.math.sqrt((np.math.fsum((dat - m_arit) ** 2)) / (n - 1))

def module_population_variance(dat):
    """ TEST SMALL ERROR
    """
    m_arit = arithmetic_mean(dat)
    n = len(dat)
    return sum(((dat - m_arit) ** 2)) / n

def module_population_standard_deviation(dat):
    """ TEST SMALL ERROR
    """
    m_arit = arithmetic_mean(dat)
    n = len(dat)
    return np.math.sqrt((np.math.fsum((dat - m_arit) ** 2)) / n)

def skewness_module_coefficient(dat):
    """ TEST SMALL ERROR
    """
    n = len(dat)
    mean = arithmetic_mean(dat)
    s = module_standard_deviation(dat)
    return (n / float(((n - 1) * (n - 2)))) * np.math.fsum(((dat - mean) / s) ** 3)

def kurtois_module_coefficient(dat):
    """ TEST STRANGE ERROR
    """

    n = len(dat)
    mean = arithmetic_mean(dat)
    s = module_standard_deviation(dat)

    a = (n * (n + 1)) / float(((n - 1) * (n - 2) * (n - 3)))
    b = sum(((dat - mean) / float(s)) ** 4)
    c = (3 * (n - 1) ** 2) / float(((n - 2) * (n - 3)))
    return ((a * b) - c)

def psRange(dat):
    element_range = max(dat) - min(dat)
    if element_range < 0:
        element_range = element_range * -1
    
    return element_range

def module_sum(dat):
    return np.math.fsum(dat)

def standard_error(dat):
    return stats.sem(dat)