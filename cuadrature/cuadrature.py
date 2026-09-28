import numpy as np

def gaussxw(N):
    """ weights and point of evaluation from legendre polynomius for gaussian cuadrature.

    The points correspond to the solutions of the legendre polynomius of the Nth degree in the interval [-1,1]

    Example:
    >>> x, w = gaussxw(2)
    >>> x 
    array([-0.57735027,  0.57735027])
    >>> w
        array([1., 1.])

    Args:
        N (int): Number of point of evaluation.

    Returns:
        tuple: Numpy arrays that contains the points of evaluation and weights.

    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    """ Scales the points an weights from Gauss-Legendre to the interval [a,b]

    Examples:
        >>> x, w = gaussxw(2)
        >>> x_new, w_new = gaussxwab(1, 3, x, w)
        >>> x_new
        array([1.42264973, 2.57735027])
        >>> w_new
        array([1., 1.])

     Args:
        a (float): Inferior limit of the integration interval
        b (float): Superior limit of the integration interval
        x (numpy.ndarray): Gauss-Legendre points on the interval [-1,1]
        w (numpy.ndarray): Associated Gauss-Legendre weights

     Returns:
        tuple: two numpy arrays with the scalated points and weights to the interval [a,b]

    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def funcEv (varInd):
    """ Evaluates the function to integrate

    Examples:
        >>> funcEv(0.0)
        0.0
    
    Args:
        varInd (float or numpy.ndarray): Value or values of the independent variable

    Returns: 
        float or numpy.ndarray: Value of the function x^6 - x^2 sin(2x).

    """
    return varInd**6 - (varInd**2) * np.sin(2 * varInd)

def calcularIntegral (integrando, a, b, tol):
    """ Evaluates the value of an integral using the Gauss-Legendre cuadrature
    
    The function increments the number of points of the cuadrature till the difference between the last consecutive aproximations is smaller than the indicated tolerance

    Examples: 
         >>> resultado, N = calcularIntegral(funcEv, 1, 3, 1e-5)
        >>> N
        7

    Args:
        integrando (callable): Function to integrate.
        a (float): Inferior limit of the integration interval.
        b (float): Superior limit of the integration interval.
        tol (float): Tolerance used as the convergence criterion.

    Returns: 
        tuple: Aproximation of the integral and the number of points used to achieve the convergence

    """
    #se definen los pesos para N= 2, 3
    x2, w2 = gaussxw(2)
    x3, w3 = gaussxw(3)

    #se hace el cambio al intervalo [1,3]
    x2, w2 = gaussxwab(a, b, x2, w2)
    x3, w3 = gaussxwab(a, b, x3, w3)

    #Probemos distintos valores de N
    I2 = np.sum(w2 * integrando(x2))
    I3 = np.sum(w3 * integrando(x3))

    i = 4
    I = I2
    I_0 = I3
    while np.abs(I-I_0) > tol:
        I = I_0
        x_0, w_0 = gaussxw (i)
        x_0, w_0 = gaussxwab (a, b, x_0, w_0)
        I_0 = np.sum(w_0 * integrando(x_0))
        i += 1

    return I_0, i-1
