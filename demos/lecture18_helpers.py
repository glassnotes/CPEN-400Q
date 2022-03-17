from pennylane import numpy as np
from scipy.linalg import sqrtm
import matplotlib.pyplot as plt

def fidelity(rho, sigma):
    """Computes the fidelity between two density matrices.
    
    Fidelity has a maximum value of 1 when the two input states are
    the same, and a minimum value of 0 when the two states are 
    totally orthogonal. When comparing the output of, e.g.,
    a state obtained through a noisy process to the ideal state,  
    higher fidelity is better.
    
    Args:
        rho (array[complex]): A density matrix.
        sigma (array[complex]): A second density matrix.
    
    Returns:
        float: The fidelity between rho and sigma.
    """
    sqrt_rho = sqrtm(rho)
    inner_thing = np.linalg.multi_dot([sqrt_rho, sigma, sqrt_rho])
    return np.real(np.trace(sqrtm(inner_thing)) ** 2)


def trace_distance(rho, sigma):
    """Computes the trace distance between two density matrices.
    
    Trace distance has a maximum value of 1 when the two input states 
    are totally orthogonal, and a minimum value of 0 when the two 
    states are the same. When comparing the output of, e.g., a state 
    obtained through a noisy process to the ideal state, lower
    trace distance is better.
    
    Args:
        rho (array[complex]): A density matrix.
        sigma (array[complex]): A second density matrix.
    
    Returns:
        float: The trace distance between rho and sigma.
    """
    rms = rho - sigma
    inner_thing = np.dot(rms.conj().T, rms)
    return np.real(0.5 * np.trace(sqrtm(inner_thing)))


def plot_density_matrix_city(rho):
    # setup the figure and axes
    fig = plt.figure(figsize=(15, 5))
    ax1 = fig.add_subplot(111, projection='3d')
    ax2 = fig.add_subplot(122, projection='3d')

    # fake data
    _x = np.arange(len(rho))
    _y = np.arange(len(rho))
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()

    real = rho.flatten().real
    imag = rho.flatten().imag

    colors_real = plt.cm.jet(real/float(real.max()))
    colors_imag = plt.cm.jet(imag/float(imag.max()))

    ax1.bar3d(x, y, np.zeros_like(x), 1, 1, real, color=colors_real, shade=False)
    ax2.bar3d(x, y, np.zeros_like(x), 1, 1, imag, color=colors_imag, shade=False)

    plt.show()