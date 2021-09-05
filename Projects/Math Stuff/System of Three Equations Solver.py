import math
import re
from re import match
import numpy as np

def getCoefficients(equation):
    # ax + by + cz = d
    eq = equation.split(' ')
    eq = ''.join(eq)
    if match('^x.+$', eq):
        eq = list(eq)
        eq[eq.index('x')] = '1x'
        eq = ''.join(eq)
    if match('^.+((\+|-)y).+$', eq):
        eq = list(eq)
        eq[eq.index('y')] = '1y'
        eq = ''.join(eq)
    if match('^.+((\+|-)z).+$', eq):
        eq = list(eq)
        eq[eq.index('z')] = '1z'
        eq = ''.join(eq)
    coefficients = re.findall('-?\d+', eq)
    for i in range(0, len(coefficients)):
        if type(coefficients[i]) != 'str':
            coefficients[i] = int(coefficients[i])
    return coefficients


equation1 = input('Equation 1 in format (ax + by + cz = d): ')
if not match('^(-|)(\d*)x ?(\+|-) ?(\d*)y ?(\+|-) ?(\d*)z ?= ?(-?\d+)$', equation1):
    print('Please enter the equation in the correct format.')
    exit(0)

equation2 = input('Equation 2 in format (ax + by + cz = d): ')
if not match('^(-|)(\d*)x ?(\+|-) ?(\d*)y ?(\+|-) ?(\d*)z ?= ?(-?\d+)$', equation2):
    print('Please enter the equation in the correct format.')
    exit(0)

equation3 = input('Equation 3 in format (ax + by + cz = d): ')
if not match('^(-|)(\d*)x ?(\+|-) ?(\d*)y ?(\+|-) ?(\d*)z ?= ?(-?\d+)$', equation3):
    print('Please enter the equation in the correct format.')
    exit(0)

eq1_c = getCoefficients(equation1)
eq2_c = getCoefficients(equation2)
eq3_c = getCoefficients(equation3)
# a b c  d
# a b c  d
# a b c  d

# 12 2 13  14
# 3 -1 3  16
# 2 6 -3  17
main_matrix = np.array([[eq1_c[0], eq1_c[1], eq1_c[2]], [eq2_c[0], eq2_c[1], eq2_c[2]], [eq3_c[0], eq3_c[1], eq3_c[2]]])
matrix_x = np.array([[eq1_c[3], eq1_c[1], eq1_c[2]], [eq2_c[3], eq2_c[1], eq2_c[2]], [eq3_c[3], eq3_c[1], eq3_c[2]]])
matrix_y = np.array([[eq1_c[0], eq1_c[3], eq1_c[2]], [eq2_c[0], eq2_c[3], eq2_c[2]], [eq3_c[0], eq3_c[3], eq3_c[2]]])
matrix_z = np.array([[eq1_c[0], eq1_c[1], eq1_c[3]], [eq2_c[0], eq2_c[1], eq2_c[3]], [eq3_c[0], eq3_c[1], eq3_c[3]]])

main_det = np.linalg.det(main_matrix)
x_det = np.linalg.det(matrix_x)
y_det = np.linalg.det(matrix_y)
z_det = np.linalg.det(matrix_z)

value_x = x_det / main_det
value_y = y_det / main_det
value_z = z_det / main_det

print(f'x={np.round(value_x, 4)}, y={np.round(value_y, 4)}, z={np.round(value_z, 4)}')
