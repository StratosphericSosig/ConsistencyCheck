# ConsistencyCheck
A python module for checking the consistency of a experimental value against the accepted value
Inorder to check the consistency of measured physical units a consistency check needs to be done
If the unit is consistent then it will follow the equation : |x[1]-x[2]| < 3(sqrt(x[3]^2 - x[4]^2)
x[1] - Accepted Scientific Value
x[2] - Measured Scientific Value
x[3] - Accepted Error
x[4] - Measured Error
