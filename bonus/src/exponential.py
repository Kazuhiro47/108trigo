from matrix_fct.matrix import *

def exp_calculus(m):
	res = add_matrix(identity_matrix(len(m)), m)
	n = 2
	while (n <= 42):
		tmp = divide_matrix_by_one_number(factorielle(n), pow_matrix(m, n))
		res = add_matrix(res, tmp)
		n += 1
	return (res)