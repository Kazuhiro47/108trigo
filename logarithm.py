from matrix import *

# ln(1 - x)
def log_1(m, progress):
	tmp = multiply_matrix_by_one_number(-1, m)
	res = substract_matrix(tmp, divide_matrix_by_one_number(2, pow_matrix(m, 2)))
	n = 2
	while (n <= 100):
		tmp = divide_matrix_by_one_number(n, pow_matrix(m, n))
		res = substract_matrix(res, tmp)
		progress.setValue(n)
		n += 1
	return (res)

# ln(1 + x)
def log_2(m, progress):
	res = substract_matrix(m, divide_matrix_by_one_number(2, pow_matrix(m, 2)))
	n = 2
	while (n <= 100):
		tmp = divide_matrix_by_one_number(n, pow_matrix(m, n))
		if (n % 2 == 0):
			add_matrix(res, tmp)
		else:
			res = substract_matrix(res, tmp)
		progress.setValue(n)
		n += 1
	return (res)