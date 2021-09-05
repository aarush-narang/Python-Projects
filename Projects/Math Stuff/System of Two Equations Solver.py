import math
import re
from re import match
import numpy as np

def getCoefficients(equation):
    eq = equation.split(' ')
    eq = ''.join(eq)
    if match('^x(\+|-)(-?\d+)y=(-?\d+)$', eq):
        eq = list(eq)
        eq[eq.index('x')] = '1x'
        eq = ''.join(eq)
    if match('^(-?\d+)x(\+|-)y=(-?\d+)$', eq):
        eq = list(eq)
        eq[eq.index('y')] = '1y'
        eq = ''.join(eq)
    coefficients = re.findall('-?\d+', eq)
    for i in range(0, len(coefficients)):
        if type(coefficients[i]) != 'str':
            coefficients[i] = int(coefficients[i])
    return coefficients


equation1 = input('Equation 1 in format (ax + by = c): ')
if not match('^(-|)(\d*)x ?(\+|-) ?(\d*)y ?= ?(-?\d+)$', equation1):
    print('Please enter the equation in the correct format.')
    exit(0)

equation2 = input('Equation 2 in format (ax + by = c): ')
if not match('^(-|)(\d*)x ?(\+|-) ?(\d*)y ?= ?(-?\d+)$', equation2):
    print('Please enter the equation in the correct format.')
    exit(0)

eq1_coefficients = getCoefficients(equation1)
eq2_coefficients = getCoefficients(equation2)

main_matrix = np.array([[eq1_coefficients[0], eq1_coefficients[1]], [eq2_coefficients[0], eq2_coefficients[1]]])
matrix_x = np.array([[eq1_coefficients[2], eq1_coefficients[1]], [eq2_coefficients[2], eq2_coefficients[1]]])
matrix_y = np.array([[eq1_coefficients[0], eq1_coefficients[2]], [eq2_coefficients[0], eq2_coefficients[2]]])

main_det = np.linalg.det(main_matrix)
x_det = np.linalg.det(matrix_x)
y_det = np.linalg.det(matrix_y)

value_x = x_det / main_det
value_y = y_det / main_det

# if math.floor(value_x) != 0 and value_x % math.floor(value_x) == 0:
#     value_x = int(value_x)
#
# if math.floor(value_y) != 0 and value_y % math.floor(value_y) == 0:
#     value_y = int(value_y)

print(f'x={np.round(value_x, 4)}, y={np.round(value_y, 4)}')
