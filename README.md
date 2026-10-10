# NUMERUS (NUmerical MEthods foR Undergraduate Scientists)

**MAKE SURE YOU READ THE `COLLABORATE.md` file before starting**

## Quick start

You need Python 3.10 or newer. Then, from the repo folder:

```bash
pip install -r requirements.txt
```

This installs `numpy` (2.0 or newer), `scipy`, `matplotlib`, `pandas` and `jupyter`. Then start Jupyter:

```bash
jupyter notebook
```

A browser tab opens. Open the `Course` folder and click `00-introduction.ipynb`. Run a cell with **Shift+Enter**, or run the whole notebook from the menu with **Run → Run All Cells** (**Kernel → Restart & Run All** for a clean start). You can also open the notebooks directly in VS Code with the Jupyter extension.

Every notebook runs top to bottom with no errors. Most take a few seconds; the slowest (A1, A4 and A5 in `Applications/`) take between half a minute and a minute and a half. To check every notebook in one go (headless, nothing is saved), run `python tools/check_notebooks.py`.

## Course map

All the chapters live together in `Course/`, numbered in reading order, with the datasets for Chapter 11 in `Course/data/`. Root finding is split over two chapters: Chapter 2 (rearrangement and bisection) and Chapter 3 (false position, Newton-Raphson, secant and friends).

All notebooks need only `numpy`, `scipy` and `matplotlib` (plus `pandas` in Chapter 0); see `requirements.txt`. Chapters 0 and 3-11 end with a **Problems** section (Chapter 3's problems cover Chapter 2 too); each applications notebook ends with **Projects**.

| Folder | Notebook | Methods covered |
| :--- | :--- | :--- |
| `Course` | `00-introduction.ipynb` | why numerical methods, limits and convergence |
| | `01-python-and-jupyter.ipynb` | Python basics |
| | `02-algebraic-and-transcendental-equations.ipynb` | rearrangement, bisection, finding a sign change in an array |
| | `03-newton-raphson-secant-and-false-position.ipynb` | false position (linear interpolation), Newton-Raphson, secant, order of convergence, Brent's method, finding all roots |
| | `04-numerical-differentiation-and-integration.ipynb` | forward/backward/central differences, round-off vs truncation, Richardson extrapolation, midpoint, trapezium, Simpson, Romberg, Gauss-Legendre, improper integrals |
| | `05-ordinary-differential-equations.ipynb` | direction fields and isoclines, Euler, Heun, Taylor series method, RK4, systems/higher-order ODEs, velocity Verlet (symplectic), adaptive step size, stiff equations and implicit Euler, shooting method |
| | `06-linear-algebra-and-eigenvalue-problems.ipynb` | Gaussian elimination, pivoting, LU decomposition, condition number, Thomas algorithm, Jacobi/Gauss-Seidel/SOR, power and inverse iteration, least squares |
| | `07-partial-differential-equations.ipynb` | FTCS, von Neumann stability, Crank-Nicolson, wave equation and CFL, upwind/Lax-Wendroff advection, relaxation for Laplace's equation |
| | `08-fourier-transforms-and-the-fft.ipynb` | DFT, recursive FFT, power spectra, aliasing, windowing, filtering, convolution theorem, spectral differentiation |
| | `09-interpolation-and-curve-fitting.ipynb` | linear and Lagrange interpolation, Runge's phenomenon, Chebyshev nodes, cubic splines, chi-squared, `curve_fit`, residuals, bootstrap |
| | `10-monte-carlo-methods.ipynb` | pseudo-random generators, MC integration, curse of dimensionality, inverse-transform and rejection sampling, importance sampling, random walks, Metropolis, simulated annealing |
| | `11-working-with-real-data.ipynb` | real data. Files in `Course/data/` (sources in `Course/data/README.md`): NOAA Mauna Loa CO2, 1958-2026 (least-squares decomposition, growth rate, spectrum); SILSO monthly sunspot numbers since 1749 (smoothing, periodogram, cycle detection, bootstrap); GWOSC strain from both LIGO detectors for GW150914 (Welch PSD, whitening, filtering, cross-correlation, matched filtering). Small published tables typed into the notebook: JPL planetary orbits and Jupiter's moons (Kepler's third law, mass of Jupiter) and NIST hydrogen Balmer wavelengths (Rydberg constant) |
| `Applications` | `A1-astrophysics.ipynb` | Kepler's equation, Lane-Emden stars and the Chandrasekhar mass, Lagrange points, N-body (figure-eight, Trojans), galaxy rotation curves |
| | `A2-quantum-mechanics.ipynb` | finite square well, Numerov shooting, matrix Hamiltonians, double-well tunnelling, hydrogen, Crank-Nicolson wavepacket scattering |
| | `A3-optics-and-waves.ipynb` | Wien's law, Fraunhofer diffraction by FFT (Airy, JWST-like mirror), Fresnel integrals, transfer-matrix thin films/Bragg mirrors, graded-index ray tracing and mirages |
| | `A4-classical-mechanics-and-chaos.ipynb` | nonlinear pendulum, driven pendulum, Poincaré sections, bifurcation diagram, Lorenz attractor, Lyapunov exponents |
| | `A5-statistical-and-thermal-physics.ipynb` | Debye/Einstein heat capacity, Fermi gas chemical potential, 2D Ising model, random walks vs diffusion |
| | `A6-electromagnetism.ipynb` | Biot-Savart and Helmholtz coils, Boris particle pusher, magnetic bottle, sparse Poisson solver for capacitance, 1D FDTD Maxwell solver |
| `Practice` | `practice-problems.ipynb` / `practice-solutions.ipynb` | 12 exercises across Chapters 2-10, each checked automatically by a `check()` cell (✅ / ❌ / ⏳ not attempted), with worked solutions |

Basic rundown of the project (the original plan; see the course map above for the chapter numbers):

### Introduction ✅

    Rationale for this resource:
    - Quick demo of Python and playthrough using some examples literally copy and paste.
    - Encouraged to break the code, you can always start again.
    - Play around with the code and see what you can screw up.

### Crash Course in Python

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

### Simple Numerical Methods:

    Solving Equations using numerical methods
    - Rearranging equations ✅ (Ch. 2)
    - linear interpolation ✅ (Ch. 3, false position)
    - Binary Chopping ✅ (Ch. 2)
    - Newton-Raphson Method ✅ (Ch. 3)
    - Iteration ✅ (Ch. 2)
    - Secant method, Brent's method ✅ (Ch. 3)

### Advanced Numerical Methods:

    Integration and differentiation
    - Trapezium Rule ✅ (Ch. 4)
    - Simpson's Rule ✅ (Ch. 4)
    - Romberg and Gaussian quadrature ✅ (Ch. 4)
    - Monte-Carlo Method ✅ (Ch. 10)
    - Finite-Difference ✅ (Ch. 4)
    - Differential Equations ✅ (Ch. 5)
    - Difference Equations ✅ (Ch. 5, 7)
    - Taylor Series Solution ✅ (Ch. 5)
    - Runge-Kutta Method ✅ (Ch. 5)
    - Isoclines ✅ (Ch. 5)
    - Higher-order Equations ✅ (Ch. 5)
    - Linear algebra and eigenvalue problems ✅ (Ch. 6)
    - PDEs ✅ (Ch. 7)
    - Interpolation and curve fitting ✅ (Ch. 9)

### Extreme Numerical Methods

    - Fourier Transforms ✅ (Ch. 8)
    - Laplace Transforms
    - Fast-Fourier Transform ✅ (Ch. 8)

### Data Structures and Algorithms

    General Overview of Computer Science Methods:
    - Hash Maps
    - Sorting Algorithms
    - Recursive Methods

### Some projects for fun...

    - Physics applications notebooks ✅ (Applications/A1-A6, each with projects)
    - Self-checking practice problems ✅ (Practice/)
    - Basic Git/Github to present projects.

<!-- if you're reading this, you read the source. Nice. -->
