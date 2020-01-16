using LinearAlgebra

function f(x, y)
    z = x*y
    if det(z) != 0
        return eigvals(z)
    end

end

A = [1 2 3; 4 5 6; 7 8 9]
B = [4 2 1; 6 2 2; 7 2 2]

println(f(A, B))
