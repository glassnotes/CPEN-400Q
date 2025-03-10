from fractions import Fraction
import numpy as np

# These functions are written based on the exercises in 
# Xanadu Quantum Codebook nodes S.3 and S.4
# https://codebook.xanadu.ai

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


def phase_to_order(phase, max_denominator):
    """Estimating which integer values divide to produce a float.
    
    Given some floating-point phase, estimate integers s, r such
    that s / r = phase, where r is no greater than some specified value.
    
    Args:
        phase (float): Some fractional value (here, will be the output
            of running QPE).
        max_denominator (int): The largest r to be considered when looking
            for s, r such that s / r = phase.
            
    Returns:
        int: The estimated value of r.
    """
    s_over_r = Fraction(phase)
    return s_over_r.limit_denominator(max_denominator).denominator
