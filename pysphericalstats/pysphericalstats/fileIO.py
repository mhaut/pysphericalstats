#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pysphericalstats.convert as pySpCconvert


def calculateAxisIncrementVector(vectors_matrix):
    fixed_vector = []
    for vector in vectors_matrix:
        fixed_vector.append(np.array([float(vector.__getitem__(3)) - float(vector.__getitem__(0)),
                                float(vector.__getitem__(4)) - float(vector.__getitem__(1)),
                                float(vector.__getitem__(5)) - float(vector.__getitem__(2))]))
    return fixed_vector

def getColumnAsArray(column_index, matrix):
    column = []
    for vector in matrix:
        for i in range(len(vector)):
            if i == column_index:
                column.append(vector[i])
    return column

def calculatePolarFormVector(incremental_vectors):
    modules_2d = []
    colatitude = []
    xy_atan = []
    polar_vectors = []
    for x, y, z in incremental_vectors:
        modules_2d.append(np.sqrt(x ** 2 + y ** 2))
        xy_atan.append(float(np.arctan(y / x)))

    for i, x in enumerate(modules_2d):
        z = incremental_vectors[i][2]
        colatitude.append(float(np.arctan(y / x)))

    # TODO colatitud y latitud negativa
    colatitude = pySpCconvert.to_sexagesimal_3d(colatitude)
    latitude   = pySpCconvert.to_sexagesimal_3d(xy_atan)

    for i, (x, y, z) in enumerate(incremental_vectors):
        polar_vectors.append([np.sqrt(x ** 2 + y ** 2 + z ** 2),
                                colatitude[i],
                                latitude[i]])
    return polar_vectors



def read_file(pathfile):
    vectors_array = []; vectorsMatrix = []
    with open(pathfile) as f:
        for line in f:
            vectorsMatrix.append([float(coordinate) for coordinate in line.split()])
    vectors_matrix = np.array(vectorsMatrix)
    if vectors_matrix.shape[1] != 6: exit()
    return np.array(vectorsMatrix)


def load_data(vectors_matrix):
    axis_inc      = calculateAxisIncrementVector(vectors_matrix)
    polar_vectors = calculatePolarFormVector(axis_inc)
    rectangular_vectors = axis_inc

    data = []
    for i, polar_element in enumerate(polar_vectors):
        vector = [pySpCconvert.calculate_vector_module(vectors_matrix[i][0],
                                                        vectors_matrix[i][1],
                                                        vectors_matrix[i][2],
                                                        vectors_matrix[i][3],
                                                        vectors_matrix[i][4],
                                                        vectors_matrix[i][5]
                                                        ),    #module
                    polar_element[0],                      #colatitud
                    polar_element[1],                      #longitud
                    rectangular_vectors.__getitem__(i)[0], #Ax
                    rectangular_vectors.__getitem__(i)[1], #Ay
                    rectangular_vectors.__getitem__(i)[2], #Az
                    vectors_matrix[i][0],                  #x0
                    vectors_matrix[i][1],                  #y0
                    vectors_matrix[i][2],                  #z0
                    vectors_matrix[i][3],                  #x1
                    vectors_matrix[i][4],                  #y1
                    vectors_matrix[i][5]]                  #z1
        data.append(vector)
    return data

def get_input_path_file():
    path = input("Enter coordinates file path: ")
    return path

def get_output_path_file():
    path = ""
    isSaving = input("Do you want to save scene scene image?(s/n): ")
    if isSaving == "s":
        path = input("Enter path for image output: ")
    return path

def transformData(vectorsMatrix):
    __fixedVectorsMatrix = []
    for vector in vectorsMatrix:
        fixedVector = [float(vector.__getitem__(0)),
                        float(vector.__getitem__(1)),
                        float(vector.__getitem__(2)),
                        float(vector.__getitem__(3)) - float(vector.__getitem__(0)),
                        float(vector.__getitem__(4)) - float(vector.__getitem__(1)),
                        float(vector.__getitem__(5)) - float(vector.__getitem__(2))]
        __fixedVectorsMatrix.append(fixedVector)
    return __fixedVectorsMatrix

def simpleLoad():
    path = '/home/pedro/PycharmProjects/test2.7/test/XYZcoor.txt'

    vectorsArray = []
    vectorsMatrix = []
    with open(path) as f:
        for line in f:
            for coordinate in line.split():
                vectorsArray.append(float(coordinate))
            vectorsMatrix.append(vectorsArray)
            vectorsArray = []

    return vectorsMatrix
