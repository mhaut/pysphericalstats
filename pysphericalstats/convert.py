#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


def to_sexagesimal_3d(radians):
    if isinstance(radians, list):
        grades = [180 * item / np.math.pi  for item in radians]
    else:
        grades = radians * 180 / np.math.pi
    return grades

def to_radian(grades):
    if isinstance(grades, list):
        radians = [item / 180 * np.math.pi  for item in grades]
    else:
        radians = grades / 180 * np.math.pi
    return radians


def calculate_vector_module(x, y, z, x1, y1, z1):
    return np.math.sqrt((x - x1)**2 + (y - y1)**2 + (z-z1)**2)


def vectors_to_rectangular(vectors):
    module, colatitud, longitud = (*vectors,)
    radian_colatitud = to_radian(colatitud)
    radian_longitud  = to_radian(longitud)
    x = np.sin(radian_colatitud) * np.cos(radian_longitud) * module
    y = np.sin(radian_colatitud) * np.sin(radian_longitud) * module
    z = np.cos(radian_colatitud)                           * module
    rectangular_vectors = np.array([x, y, z])
    return rectangular_vectors


def vectorsToPolar(incremental_vectors):
    num_data = incremental_vectors.shape[0]
    x = incremental_vectors[:, 0]
    y = incremental_vectors[:, 1]
    z = incremental_vectors[:, 2]
    modules_2d = np.sqrt(x**2 + y**2)
    colatitud = np.arctan(modules_2d / z)
    colatitud[np.isnan(colatitud)] == 0
    colatitud[colatitud < 0] += np.pi
    colatitud  = to_sexagesimal_3d(colatitud)
    longitud   = to_sexagesimal_3d(np.arctan(y / x))
    longitud[x < 0] += 180.
    longitud[longitud < 0] += 360.
    polar_vectors = np.zeros((num_data, 3))
    polar_vectors[:, 0] = np.sqrt(x**2 + y**2 + z**2)
    polar_vectors[:, 1] = colatitud
    polar_vectors[:, 2] = longitud
    return polar_vectors

def vector_to_polar(vector_matrix):
    x, y, z = (*np.array(vector_matrix).T, )
    num_data = x.size
    module2D  = np.sqrt(x**2 + y**2)
    colatitud = np.arctan(module2D / z)
    colatitud[np.isnan(colatitud)] = 0
    colatitud[colatitud < 0] += np.math.pi
    colatitud = to_sexagesimal_3d(colatitud)
    longitud  = to_sexagesimal_3d(np.arctan(y / x))
    longitud[np.isnan(longitud)] = 0
    longitud[x < 0] += 180
    longitud[longitud < 0] += 360
    polar_vectors = np.array([np.sqrt(x ** 2 + y ** 2 + z ** 2),
                                colatitud,
                                longitud])
    return polar_vectors
