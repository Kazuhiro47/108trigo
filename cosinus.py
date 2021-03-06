from matrix import *

def cos_calculus(m, progress):
	tmp = divide_matrix_by_one_number(factorielle(2), pow_matrix(m, 2))
	res = substract_matrix(identity_matrix(len(m)), tmp)
	n = 2
	while (n <= 100):
		tmp = divide_matrix_by_one_number(factorielle(2 * n), pow_matrix(m, 2 * n))
		if (n % 2 == 0):
			res = add_matrix(res, tmp)
		else:
			res = substract_matrix(res, tmp)
		progress.setValue(n)
		n += 1
	return (res)

def cosh_calculus(m, progress):
	tmp = divide_matrix_by_one_number(factorielle(2), pow_matrix(m, 2))
	res = add_matrix(identity_matrix(len(m)), tmp)
	n = 2
	while (n <= 100):
		tmp = divide_matrix_by_one_number(factorielle(2 * n), pow_matrix(m, 2 * n))
		res = add_matrix(res, tmp)
		progress.setValue(n)
		n += 1
	return (res)