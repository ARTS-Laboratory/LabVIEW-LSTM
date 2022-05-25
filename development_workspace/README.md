# Package

VIs visible from the function palette are "Create Dense Cell.vi", "Create LSTM Cell.vi", "sigmoid.vi", "tanh.vi", "ReLU.vi", and "Vector Elementwise Multiplication.vi". Those first two are what are used to create the LSTM cell and dense cell VIs. The others are used within the LSTM equations and may be useful for other machine learning applications.

## 'Create Cell' VIs
### v1.0
1. Operable but not ideal. To access the functions panel, the user must open a blank VI only to then click into the fill-template VI. The generated VIs initially save to the package's folder.
2. Will probably change the name to "Create LSTM Cell.vi" and "Create Dense Cell.vi" for the next version.
### v1.1
1. Changed names.
2. No longer takes transposed matrices as input.
3. Still saves VI to package's folder.
4. (v1.1.2) Fixed Create Dense Cell to include bias term
### v1.2
1. Added GRU Cell (not tested, no python conversion function)
## sigmoid.vi, tanh.vi, and ReLU.vi
Elementwise sigmoid and tanh functions.
### v1.0
1. The linear constants right now are not optimal.
2. Performance improvement can be gained by using a 'minimum cascade' implementation.
### v1.1
1. Changed to optimal constants, use the minimum cascade.
2. (v1.1.1) Changed to 'true' functions (not piecewise approximations). Showed little/no reduction in speed of forward pass, more deterministic timing.
3. (v1.1.2) Added ReLU.vi
