from re import match, findall
import numpy as np


def findRoots(equation):
    eq = equation.split(' ')
    eq = ''.join(eq)

    if match('^y=(-|)x\^2.+$', eq):
        eq = list(eq)
        if eq[eq.index('x')+1] == '^':
            eq[eq.index('x')] = '1x'
        eq = ''.join(eq)
    if match('^.+((\+|-)x).+$', eq):
        eq = list(eq)
        eq2 = list(eq)
        if eq[eq.index('x')+1] == '^':
            del eq2[eq.index('x')]
            eq[eq2.index('x')+1] = '1x'
        eq = ''.join(eq)
    if not match('^y=((-|)(\d+|)x\^2)((\+|-)(\d+|)x)((\+ ?\d+|- ?\d+))$', eq):
        eq = list(eq)
        eq.append('+0')
        eq = ''.join(eq)
    coefficients = findall('-?\d+', eq)
    for i in range(0, len(coefficients)):
        if type(coefficients[i]) != 'str':
            coefficients[i] = int(coefficients[i])
    del coefficients[1]
    roots = np.roots(coefficients)
    return roots

exp = input('Enter quadratic equation in form "y = ax^2 + bx + c" to find roots: ')
if not match('y ?= ?((-|)(\d+|)x\^2) ?((\+|-) ?(\d+|)x) ?((\+ ?\d+|- ?\d+|))', exp):
    print('Please enter the equation in the correct format.')
    exit(0)

print(f'x = {findRoots(exp)[0]}, {findRoots(exp)[1]}')

