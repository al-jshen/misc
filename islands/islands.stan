data {
    int<lower=1> n;
    vector[n] population;
    int tools[n];
    matrix[n, n] distances;
}

transformed data {
    matrix[n, n] jitter = diag_matrix(rep_vector(0.01, n));
    vector[n] zeros = rep_vector(0., n);
}

parameters {
    vector<lower=-1, upper=1>[n] k;

    real<lower=0> p_alpha;
    real<lower=0> p_beta;
    real<lower=0> p_gamma;
    real<lower=0> eta_sq;
    real<lower=0> rho_sq;
}

transformed parameters {
    vector[n] expected_tools = exp(k) * p_alpha .* pow(population, p_beta) / p_gamma;
    matrix[n, n] K = eta_sq * exp(-rho_sq * square(distances)) + jitter;
}

model {
    tools ~ poisson(expected_tools);
    
    k ~ multi_normal(zeros, K);
    
    p_alpha ~ exponential(1);
    p_beta ~ exponential(1);
    p_gamma ~ exponential(1);
    
    eta_sq ~ exponential(2);
    rho_sq ~ exponential(0.5);
}
