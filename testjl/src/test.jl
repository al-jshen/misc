using ForwardDiff;

f(x) = 2x^2 + x
println(
  ForwardDiff.derivative(f, 2.)
)

