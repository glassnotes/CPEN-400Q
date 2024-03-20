import numpy as np

def convert_matrix_to_sun(U):
    r"""Convert a matrix from U(N) to SU(N).

    Args:
        U (array[complex]): A unitary matrix

    Returns:
        array[complex]: A matrix in SU(N) (i.e., with determinant 1) that is
        equivalent to U up to a global phase.
    """
    det = np.linalg.det(U)
    exp_angle = -1j * det / U.shape[0]
    return U * np.exp(exp_angle)

def fractional_binary_to_float(sample):
    """Convert an n-bit sample [k1, k2, ..., kn] to a floating point 
    value using fractional binary representation,
    
        k = (k1 / 2) + (k2 / 2 ** 2) + ... + (kn / 2 ** n)
        
    Args:
        sample (list[int] or array[int]): A list or array of bits, e.g.,
            the sample output of quantum circuit.
            
    Returns:
        float: The floating point value corresponding computed from the
        fractional binary representation.
    """
    return np.sum(
        [int(sample[bit]) / 2 ** (bit + 1) for bit in range(len(sample))]
    )

def get_phase_window(probs):
    """Given a list of outcome probabilities from phase estimation,
    compute the window in which the phase should lie.
    
        k = (k1 / 2) + (k2 / 2 ** 2) + ... + (kn / 2 ** n)
        
    Args:
        sample (list[int] or array[int]): A list or array of bits, e.g.,
            the sample output of quantum circuit.
            
    Returns:
        float: The floating point value corresponding computed from the
        fractional binary representation.
    """
    n_qubits = int(np.log2(len(probs)))
    two_most_probable = np.argsort(probs)[-2:]
    lower_bound = fractional_binary_to_float(np.binary_repr(two_most_probable[0], n_qubits))
    upper_bound = fractional_binary_to_float(np.binary_repr(two_most_probable[1], n_qubits))

    return lower_bound, upper_bound
