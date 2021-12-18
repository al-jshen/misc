cd("/home/js/programs/misc/islands")
using Pkg
Pkg.activate(".")
Pkg.add("Turing")
Pkg.add("CSV")
Pkg.add("DataFrames")
Pkg.add("LinearAlgebra")
Pkg.add("StatsPlots")
Pkg.add("Plots")
Pkg.precompile()
using Turing, CSV
using DataFrames, LinearAlgebra
using StatsPlots, Plots

islands = CSV.File("./islands.csv")
distances = CSV.File("./island_distance_matrices.csv"; delim = ",", types=Float64) |> Tables.matrix
distances

@model model_islands(n, populations, tools, distances) = begin
    p_alpha ~ Exponential(1)
    p_beta ~ Exponential(1)
    p_gamma ~ Exponential(1)

    eta_sq ~ Exponential(2)
    rho_sq ~ Exponential(0.5)

    K = eta_sq * exp.(-rho_sq .* distances .* distances) + I .* 0.01
    k ~ MvNormal(zeros(n), K)
    
    expected_tools = exp.(k) * p_alpha .* (populations .^ p_beta) ./ p_gamma
    for i in 1:n
        tools[i] ~ Poisson(expected_tools[i])
    end
end
   

chains = sample(model_islands(10, islands.population, islands.total_tools, distances), NUTS(), MCMCThreads(), 1000, 4)

summary = describe(chains)
summary[1]
summary[2]

plot(chains)

chains[:p_alpha].data |> (x -> (mean(x), std(x)))

corr = function(etasq, rhosq, dist)
    k = etasq .* exp.(-rhosq .* dist .* dist)
end

distgen = reshape(collect(0:0.01:20), (1, :))
corgen = corr(reshape(chains[:eta_sq].data, :), reshape(chains[:rho_sq].data, :), distgen)
distgen = reshape(distgen, :)

plot(distgen, corgen[1,:], color="black", alpha=0.3, lw=1.5)
ylims!((0, 2.5))

for i in rand(1:4000, 100)
    display(plot!(distgen, corgen[i,:], color="black", alpha=0.3, lw=1.5))
end
