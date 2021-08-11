using ForwardDiff

f(x) = 2x^2 + x
ForwardDiff.derivative(f, 2.)

