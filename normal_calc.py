from matrix import *

# 1 / (1 - x)
def inverted_fct_1(m, progress):
	res = add_matrix(identity_matrix(len(m)), m)
	n = 2
	while (n <= 100):
		res = add_matrix(res, pow_matrix(m, n))
		progress.setValue(n)
		n += 1
	return (res)

# 1 / (1 + x)
def inverted_fct_2(m, progress):
	res = substract_matrix(identity_matrix(len(m)), m)
	n = 2
	while (n <= 100):
		if (n % 2 == 0):
			res = add_matrix(res, pow_matrix(m, n))
		else:
			res = substract_matrix(res, pow_matrix(m, n))
		progress.setValue(n)
		n += 1
	return (res)