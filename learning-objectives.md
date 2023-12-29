# Course learning objectives

## Module 1: the basics (states, gates, measurements, and circuits)
 - perform quantum computations using Dirac notation and matrix algebra
 - express quantum computations using quantum circuits
 - program quantum circuits in PennyLane
 - use the Bloch sphere to represent states and the action of quantum operations
 - list and define the core set of elementary quantum operations
 - define and give examples of entangled states
 - compute the result of measurements on one or more qubits in multiple bases
 - use Bell basis measurements to implement superdense coding and teleportation
 - describe the structure of variational quantum algorithms
 
## Module 2: oracle-based algorithms, complexity, and quantum resources
 - explain what it means for an algorithm to have a quantum speedup
 - define quantum oracles and query complexity 
 - implement oracles and Grover's algorithm in PennyLane
 - identify the different components of the quantum compilation stack
 - define and list common universal gate sets
 - estimate the resources required to run a quantum algorithm
 - implement quantum transforms to perform simple circuit optimization
   in PennyLane

## Module 3: QFT-based algorithms
 - define and state the scaling of the quantum Fourier transform
 - implement the quantum Fourier transform in PennyLane
 - use quantum phase estimation (QPE) to estimate the eigenvalues of a unitary matrix
 - use QPE to implement order finding, and simulate Shor's factoring algorithm
 - identify cryptographic schemes that are susceptible to quantum attack
 - implement an alternative key distribution protocol based on quantum
   mechanics, and describe conditions under which it is robust to quantum attack

## Module 4: simulating physical systems
 - describe physical systems using Hamiltonians
 - Trotterize a Hamiltonian and state key bounds on the approximation accuracy
   of the simulations
 - construct quantum circuits to simulate time evolution of quantum systems
 - use QPE to determine the ground state energy of a quantum system
 - implement a variational quantum eigensolver to determine the ground state
   energy of a quantum system, and discuss its limitations
   
## Module 5: characterizing noise in quantum systems
 - represent quantum states and measurements in the density matrix formalism
 - express quantum operations as quantum channels, and state their key
   mathematical properties 
 - discuss the strengths and limitations of key metrics used to quantify the
   performance of today's quantum computers
 - perform quantum state tomography using PennyLane
 - describe the randomized benchmarking protocol, and apply it to estimate the
   average gate fidelity for a simulated noisy system
