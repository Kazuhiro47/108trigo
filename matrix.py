from sys import stdout

def create_matrix(y, x, filler):
    return [[filler] * x for _ in range(y)]

def print_matrix(mat):
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			if (j + 1 != len(mat[i])):
				stdout.write(str(mat[i][j]) + "\t")
			else:
				stdout.write(str(mat[i][j]))
		stdout.write("\n")

def multiply_matrix(mat1, mat2):
	if (len(mat1[0]) != len(mat2)):
		print("Can't multiply matrix with different length in mat1 x and mat 2 y")
		return (-1)
	result = create_matrix(len(mat1), len(mat2[0]), 0)
	k = 0
	for i in range(len(mat1)):
		for j in range(len(mat2[0])):
			for l in range(len(mat1[0])):
				result[i][j] += mat1[i][l] * mat2[l][j]
	return (result)