data {
  int<lower=1> N;
  vector[N] x;
  vector[N] y;
}

parameters {
  real m;
  real b;
  real s;
}

model {
  y ~ normal(x * m + b, s);
}
