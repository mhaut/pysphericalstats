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
    radians = []
    if isinstance(grades, list):
        radians = [item / 180 * np.math.pi  for item in grades]
    else:
        radians = (grades / 180 * np.math.pi)
    return radians


def calculate_vector_module(x, y, z, x1, y1, z1):
    return np.math.sqrt(((x - x1)**2) + ((y - y1)**2) + ((z-z1)**2))


def vectors_to_rectangular(vectors):
    module    = vectors[0]
    colatitud = vectors[1]
    longitude = vectors[2]

    radian_colatitude = to_radian(colatitud)
    radian_longitude  = to_radian(longitude)

    x = np.sin(radian_colatitude) * np.cos(radian_longitude) * module
    y = np.sin(to_radian(colatitud)) * np.sin(to_radian(longitude)) * module
    z = np.cos(to_radian(colatitud)) * module

    rectangular_vectors = (x, y, z)
    return rectangular_vectors


def vector_to_polar(vector_matrix):
    modules_2d = []
    colatitud = []
    xy_atan = []
    polar_vectors = []
    z = []
    i = 0

    while i < ArithmeticUtil.number_of_elements(vector_matrix[0]):
        x = vector_matrix[0][i]
        y = vector_matrix[1][i]
        z = vector_matrix[2][i]
        modules_2d.append(np.math.sqrt(x ** 2 + y ** 2))
        xy_atan.append(np.arctan(y / x))
        i +=1

    for i, x in enumerate(modules_2d):
        y = vector_matrix[1][i]
        aux = np.math.atan(y / x)
        if aux < 0:
            aux += np.math.pi
        colatitud.append(aux)

    colatitud = to_sexagesimal_3d(colatitud)
    longitud  = to_sexagesimal_3d(xy_atan)

    fixed_longitud = []
    for aux in longitud:
        if aux < 0:
            aux +=360
        fixed_longitud.append(aux)


    i = 0
    while i < len(vector_matrix[0]):
        x = vector_matrix[0][i]
        y = vector_matrix[1][i]
        z = vector_matrix[2][i]
        polar_vectors.append([np.math.sqrt(x ** 2 + y ** 2 + z ** 2),
                                colatitud[i],
                                fixed_longitud[i]])
        i += 1

    return polar_vectors








