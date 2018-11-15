import math

def make_translate( x, y, z ):
	return [[1, 0, 0, x],
		[0, 1, 0, y],
		[0, 0, 1, z],
		[0, 0, 0, 1]]

def make_scale( x, y, z ):
	return [[x, 0, 0, 0],
		[0, y, 0, 0],
		[0, 0, z, 0],
		[0, 0, 0, 1]]
    
def make_rotX( theta ):
	return [[1, 0, 0, 0],
		[0, math.cos(theta), -math.sin(theta), 0],
		[0, math.sin(theta), math.cos(theta), 0],
		[0, 0, 0, 1]]

def make_rotY( theta ):
	return [[math.cos(theta), 0, math.sin(theta), 0],
		[0, 1, 0, 0],
		[-math.sin(theta), 0, math.cos(theta), 0],
		[0, 0, 0, 1]]

def make_rotZ( theta ):
	return [[math.cos(theta), -math.sin(theta), 0, 0],
		[math.sin(theta), math.cos(theta), 0, 0], 
		[0, 0, 1, 0],
		[0, 0, 0, 1]]

def new_matrix(rows = 4, cols = 4):
	return [[0 for r in range(rows)] for c in range(cols)]

def print_matrix(matrix):
	for r in matrix:
		print r

def transpose(matrix):
	return [[matrix[j][i]for j in range(len(matrix))] for i in range(len(matrix[0]))]

def ident(matrix):
	return [[i == j for j in range(len(matrix[0]))] for i in range(len(matrix))]

def scalar_mult(matrix, x):
	return [[x*e for e in row] for row in matrix]

def matrix_mult(m1, m2):
	return [[sum(m1[r][i]*m2[i][c] for i in range(len(m2))) for c in range(len(m2[0]))] for r in range(len(m1))]

