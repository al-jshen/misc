use compute::distributions::*;

const ALPHA: f64 = 5.;
const BETA: f64 = 2.;
const SIGMA: f64 = 10.;

fn main() {
    let scatter = Normal::new(0., SIGMA);
    let xs = (0..=100).map(|x| x as f64).collect::<Vec<_>>();
    let ys = &xs
        .iter()
        .map(|x| ALPHA + BETA * x + scatter.sample())
        .collect::<Vec<_>>();
    println!("{:?}", xs);
    println!("{:?}", ys);
    let alpha = 5.;
    let beta = 2.2;
    let sigma = 15.;
    let distalpha = Normal::new(alpha, 2.);
    let distbeta = Normal::new(beta, 0.5);
    let mu = &xs.iter().map(|x| alpha + beta * x).collect::<Vec<_>>();
    let distmu = &mu
        .iter()
        .map(|x| Normal::new(*x, sigma))
        .collect::<Vec<_>>();
    let likelihood = &distmu
        .iter()
        .enumerate()
        .map(|(i, x)| x.pdf(ys[i]).ln())
        .sum::<f64>();
    println!("{}", likelihood);
    // let pred = Normal::new(mu, sigma);
}
