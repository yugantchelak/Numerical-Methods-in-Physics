# NUMERUS (NUmerical MEthods foR Undergraduate Scientists)

**MAKE SURE YOUR READ THE `COLLABORATE.md` file before starting**

## Course map

All notebooks need only `numpy`, `scipy` and `matplotlib` (plus `pandas` in Chapter 0). Each course chapter ends with a **Problems** section; each applications notebook ends with **Projects**.

| Folder | Notebook | Methods covered |
| :--- | :--- | :--- |
| `Course/00 Introduction` | `00. Introduction.ipynb` | why numerical methods, limits and convergence |
| `Course/01 Crash Course in Python and Jupyter` | `01. Python and Jupyter.ipynb` | Python basics |
| `Course/03 Algebraic and Transcendental Equations` | `03-algebraic-and-transcendental-equations.ipynb` | rearrangement, bisection |
| | `03b-newton-raphson-secant-and-false-position.ipynb` | false position (linear interpolation), Newton-Raphson, secant, order of convergence, Brent's method, finding all roots |
| `Course/04 Numerical Differentiation and Integration` | `04-numerical-differentiation-and-integration.ipynb` | forward/backward/central differences, round-off vs truncation, Richardson extrapolation, midpoint, trapezium, Simpson, Romberg, Gauss-Legendre, improper integrals |
| `Course/05 Ordinary Differential Equations` | `05-ordinary-differential-equations.ipynb` | direction fields and isoclines, Euler, Heun, Taylor series method, RK4, systems/higher-order ODEs, velocity Verlet (symplectic), adaptive step size, stiff equations and implicit Euler, shooting method |
| `Course/06 Linear Algebra and Eigenvalue Problems` | `06-linear-algebra-and-eigenvalue-problems.ipynb` | Gaussian elimination, pivoting, LU decomposition, condition number, Thomas algorithm, Jacobi/Gauss-Seidel/SOR, power and inverse iteration, least squares |
| `Course/07 Partial Differential Equations` | `07-partial-differential-equations.ipynb` | FTCS, von Neumann stability, Crank-Nicolson, wave equation and CFL, upwind/Lax-Wendroff advection, relaxation for Laplace's equation |
| `Course/08 Fourier Transforms and the FFT` | `08-fourier-transforms-and-the-fft.ipynb` | DFT, recursive FFT, power spectra, aliasing, windowing, filtering, convolution theorem, spectral differentiation |
| `Course/09 Interpolation and Curve Fitting` | `09-interpolation-and-curve-fitting.ipynb` | linear and Lagrange interpolation, Runge's phenomenon, Chebyshev nodes, cubic splines, chi-squared, `curve_fit`, residuals, bootstrap |
| `Course/10 Monte Carlo Methods` | `10-monte-carlo-methods.ipynb` | pseudo-random generators, MC integration, curse of dimensionality, inverse-transform and rejection sampling, importance sampling, random walks, Metropolis, simulated annealing |
| `Course/11 Working with Real Data` | `11-working-with-real-data.ipynb` | real datasets in `data/`: Mauna Loa CO2 (least-squares decomposition, growth rate, spectrum), 275 years of sunspots (smoothing, periodogram, cycle detection, bootstrap), Kepler's law and Jupiter's mass, the Rydberg constant from NIST Balmer lines, and GW150914 LIGO strain (Welch PSD, whitening, filtering, cross-correlation, matched filtering) |
| `Applications` | `A1-astrophysics.ipynb` | Kepler's equation, Lane-Emden stars and the Chandrasekhar mass, Lagrange points, N-body (figure-eight, Trojans), galaxy rotation curves |
| | `A2-quantum-mechanics.ipynb` | finite square well, Numerov shooting, matrix Hamiltonians, double-well tunnelling, hydrogen, Crank-Nicolson wavepacket scattering |
| | `A3-optics-and-waves.ipynb` | Wien's law, Fraunhofer diffraction by FFT (Airy, JWST-like mirror), Fresnel integrals, transfer-matrix thin films/Bragg mirrors, graded-index ray tracing and mirages |
| | `A4-classical-mechanics-and-chaos.ipynb` | nonlinear pendulum, driven pendulum, Poincaré sections, bifurcation diagram, Lorenz attractor, Lyapunov exponents |
| | `A5-statistical-and-thermal-physics.ipynb` | Debye/Einstein heat capacity, Fermi gas chemical potential, 2D Ising model, random walks vs diffusion |
| | `A6-electromagnetism.ipynb` | Biot-Savart and Helmholtz coils, Boris particle pusher, magnetic bottle, sparse Poisson solver for capacitance, 1D FDTD Maxwell solver |
| `Practice` | `practice-problems.ipynb` / `practice-solutions.ipynb` | 12 self-checking exercises across Chapters 3-10, with worked solutions |

Basic rundown of the project:

### 0. Introduction ✅

    Rationale for this resource:
    - Quick demo of Python and playthrough using some examples literally copy and paste.
    - Encouraged to break the code, you can always start again.
    - Play around with the code and see what you can screw up.

### 1. Crash Course in Python

    a. Introduction to Python, what it is and how to use it:
    - definition of python ✅
    - data types (`int`, `string`, `dict`...) 🟨
    - definitions of data-types and important methods
    - conditional logic, loops (`for`, `while`), useful operators etc.
    - methods and functions (built-in and custom)
    - classes
    - OOP (object-oriented programming) ?
    - decorators
    - generators

    b. Important python packages (`numpy`, `matplotlib`, `scipy`,`pandas`...)
    - introduction to numpy and matplotlib (pyplot) docs
    - using scipy for integration and differentiation

    c. Modules and organising file structure.

### 2. Simple Numerical Methods:

    Solving Equations using numerical methods
    - Rearranging equations ✅
    - linear interpolation ✅ (03b, false position)
    - Binary Chopping ✅ (03 + 03b)
    - Newton-Raphson Method ✅ (03b)
    - Iteration ✅
    - Secant method, Brent's method ✅ (03b)

### 3. Advanced Numerical Methods:

    Integration and differentiation
    - Trapezium Rule ✅ (04)
    - Simpson's Rule ✅ (04)
    - Romberg and Gaussian quadrature ✅ (04)
    - Monte-Carlo Method ✅ (10)
    - Finite-Difference ✅ (04)
    - Differential Equations ✅ (05)
    - Difference Equations ✅ (05, 07)
    - Taylor Series Solution ✅ (05)
    - Runge-Kutta Method ✅ (05)
    - Isoclines ✅ (05)
    - Higher-order Equations ✅ (05)
    - Linear algebra and eigenvalue problems ✅ (06)
    - PDEs ✅ (07)
    - Interpolation and curve fitting ✅ (09)

### 4. Extreme Numerical Methods

    - Fourier Transforms ✅ (08)
    - Laplace Transforms
    - Fast-Fourier Transform ✅ (08)

### 5. Data Structures and Algorithms

    General Overview of Computer Science Methods:
    - Hash Maps
    - Sorting Algorithms
    - Recursive Methods

### Some projects for fun...

    - Physics applications notebooks ✅ (Applications/A1-A6, each with projects)
    - Self-checking practice problems ✅ (Practice/)
    - Basic Git/Github to present projects.

<!-- if you're reading this, you read the source. Nice. -->
