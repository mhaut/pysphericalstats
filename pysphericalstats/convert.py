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
    module    = vectors[0]
    colatitud = vectors[1]
    longitude = vectors[2]
    radian_colatitude = to_radian(colatitud)
    radian_longitude  = to_radian(longitude)
    x = np.sin(radian_colatitude) * np.cos(radian_longitude) * module
    y = np.sin(radian_colatitude) * np.sin(radian_longitude) * module
    z = np.cos(radian_colatitude) * module
    rectangular_vectors = [x, y, z]
    return rectangular_vectors


def vector_to_polar(vector_matrix):
    vector_matrix = np.array(vector_matrix).T
    num_data = vector_matrix.shape[0]
    x = vector_matrix[:,0]
    y = vector_matrix[:,1]
    z = vector_matrix[:,2]
    module2D  = np.sqrt(x**2 + y**2)
    colatitud = np.arctan(module2D / z)
    colatitud[np.isnan(colatitud)] = 0
    colatitud[colatitud < 0] += np.math.pi
    colatitud = to_sexagesimal_3d(colatitud)
    longitud  = to_sexagesimal_3d(np.arctan(y / x))
    longitud[np.isnan(longitud)] = 0
    longitud[x < 0] += 180
    longitud[longitud < 0] += 360

    polar_vectors =[np.sqrt(x ** 2 + y ** 2 + z ** 2),
                    colatitud,
                    longitud]
    return polar_vectors
