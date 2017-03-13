from bonus.matrix_fct.matrix import *

# 1 / (1 - x)
def inverted_fct_1(m):
	res = add_matrix(identity_matrix(len(m)), m)
	n = 2
	while (n <= 42):
		res = add_matrix(res, pow_matrix(m, n))
		n += 1
	return (res)

# 1 / (1 + x)
def inverted_fct_2(m):
	res = substract_matrix(identity_matrix(len(m)), m)
	n = 2
	while (n <= 42):
		if (n % 2 == 0):
			res = add_matrix(res, pow_matrix(m, n))
		else:
			res = substract_matrix(res, pow_matrix(m, n))
		n += 1
	return (res)