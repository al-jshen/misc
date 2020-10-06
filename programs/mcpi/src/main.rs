use rayon::prelude::*;

fn main() {
    let n = 1e8 as usize;
    let dat = (0..n)
        .into_par_iter()
        .map(|_| (fastrand::f32(), fastrand::f32()))
        .collect::<Vec<_>>();
    let in_circ: isize = dat.par_iter().map(|x| (normsq2d(x) < 1.) as isize).sum();
    println!("{:?}", 4. * in_circ as f32 / n as f32);
}

fn normsq2d(xy: &(f32, f32)) -> f32 {
    xy.0.powi(2) + xy.1.powi(2)
}
