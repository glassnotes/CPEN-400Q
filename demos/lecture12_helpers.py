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


def get_U_Na(N, a):
    """Computes the unitary matrix U_(N, a) used in the order-finding
    portion of Shor's algorithm.
    
    U_(N, a) multiples a computational basis state by a modulo N, i.e.,
        U_(N, a) |k> = |ak mod N>
        
    In Shor's algorithm, we try to find its order, i.e., the smallest
    m such that 
        U_(N, a)^m |k> = |k mod N> = |k>
    
    Args:
        N (int): The modulus. In Shor's algorithm, this is the number 
            we are trying to find the prime factors of.
        a (int): The candidate value a which we are testing to try and
            find a non-trivial square root (which will then allow us to
            recover the prime factors of N).
            
    Returns:
        array[int]: The matrix representation U_(N, a).
    """    
    # Compute size of the matrix; we need at least log2(N) qubits
    # because we are looking at computational basis states modulo N
    n_qubits = int(np.ceil(np.log2(N)))
    
    U_Na = np.zeros([2 ** n_qubits, 2 ** n_qubits])
    
    # U_Na is a permutation matrix; for each k < N, need to compute
    # |l> = |a k mod N>, and then set the value of U_Na[l, k] = 1
    for k in range(N):
        U_Na[(k * a) % N, k] = 1

    # We might have more basis states than we need, if N < 2 ** n_qubits
    # so we set the remaining rows to identity rows
    for extra in range(N, 2 ** n_qubits):
        U_Na[extra, extra] = 1
        
    return U_Na