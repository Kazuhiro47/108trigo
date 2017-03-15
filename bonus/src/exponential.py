from matrix_fct.matrix import *

def exp_calculus(m, progress):
	res = add_matrix(identity_matrix(len(m)), m)
	n = 2
	while (n <= 100):
		tmp = divide_matrix_by_one_number(factorielle(n), pow_matrix(m, n))
		res = add_matrix(res, tmp)
		progress.setValue(n)
		n += 1
	return (res)