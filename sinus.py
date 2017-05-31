from matrix import *

def sin_calculus(m, progress):
	tmp = divide_matrix_by_one_number(factorielle(3), pow_matrix(m, 3))
	res = substract_matrix(m, tmp)
	n = 2
	while (n <= 100):
		tmp = divide_matrix_by_one_number(factorielle(2 * n + 1), pow_matrix(m, 2 * n + 1))
		if (n % 2 == 0):
			res = add_matrix(res, tmp)
		else:
			res = substract_matrix(res, tmp)
		progress.setValue(n)
		n += 1
	return (res)

def sinh_calculus(m, progress):
	tmp = divide_matrix_by_one_number(factorielle(3), pow_matrix(m, 3))
	res = add_matrix(m, tmp)
	n = 2
	while (n <= 100):
		tmp = divide_matrix_by_one_number(factorielle(2 * n + 1), pow_matrix(m, 2 * n + 1))
		res = add_matrix(res, tmp)
		progress.setValue(n)
		n += 1
	return (res)