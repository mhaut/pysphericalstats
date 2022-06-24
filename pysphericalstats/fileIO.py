#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pysphericalstats.convert as pySpCconvert


def calculateAxisIncrementVector(vectors_matrix):
    fixed_vector = np.zeros((vectors_matrix.shape[0],vectors_matrix.shape[1]//2))
    for i in range(3):
        fixed_vector[:, i] = vectors_matrix[:, i+3] - vectors_matrix[:, i]
    return fixed_vector


def read_file(pathfile):
    vectors_array = []; vectorsMatrix = []
    with open(pathfile) as f:
        for line in f:
            vectorsMatrix.append([float(coordinate) for coordinate in line.split()])
    vectors_matrix = np.array(vectorsMatrix)
    if vectors_matrix.shape[1] != 6: exit()
    return np.array(vectorsMatrix)


def load_data(vectors_matrix, type_file=1):
    if type_file == 1:
        axis_inc      = calculateAxisIncrementVector(vectors_matrix)
        polar_vectors = pySpCconvert.vectorsToPolar(axis_inc) # TODO: CAMBIADO DE calculatePolarFormVector
        rectangular_vectors = axis_inc
    elif type_file == 2: # ALERT: ESTO HAY QUE REVISAR
        polar_vectors = pySpCconvert.vectorsToPolar(vectors_matrix) # TODO: CAMBIADO DE calculatePolarFormVector
        rectangular_vectors = vectors_matrix
    elif type_file == 3: # ALERT: ESTO HAY QUE REVISAR
        polar_vectors = vectors_matrix
        rectangular_vectors = pySpCconvert.vectors_to_rectangular(vectors_matrix)
    
    data = np.zeros((len(polar_vectors), 12))
    for i, polar_element in enumerate(polar_vectors):
        data[i,:] = [pySpCconvert.calculate_vector_module(*vectors_matrix[i,:6]),  # module
                    *polar_element[:2],                                            # colatitud, longitud
                    *rectangular_vectors[i, :3],                                   # Ax, Ay, Az
                    *vectors_matrix[i, :6]]                                        # x0, y0, z0, x1, y1, z1
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
    fixed_vector = np.zeros((vectorsMatrix.shape))
    for i in range(3):
        fixed_vector[:, i] = vectors_matrix[:, i]
        fixed_vector[:, i+3] = vectors_matrix[:, i+3] - vectors_matrix[:, i]
    return fixed_vector

