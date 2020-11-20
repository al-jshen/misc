#![feature(test)]
extern crate test;
use compute::distributions::{DiscreteUniform, Distribution};

pub fn swap_xor(a: &mut i64, b: &mut i64) {
    *a = *a ^ *b;
    *b = *b ^ *a;
    *a = *a ^ *b;
}

pub fn swap_temp(a: &mut i64, b: &mut i64) {
    let temp_a = *a;
    *a = *b;
    *b = temp_a;
}

pub fn swap_std(a: &mut i64, b: &mut i64) {
    std::mem::swap(a, b);
}

pub fn gen_vecs() -> (Vec<i64>, Vec<i64>) {
    let sampler = DiscreteUniform::new(0, 1000);
    (
        sampler.sample_iter(100).iter().map(|v| *v as i64).collect(),
        sampler.sample_iter(100).iter().map(|v| *v as i64).collect(),
    )
}

#[cfg(test)]
mod tests {
    use super::*;
    use test::Bencher;

    #[bench]
    fn bench_swap_xor(b: &mut Bencher) {
        let (mut x, mut y) = gen_vecs();
        let prev_x = x.clone();
        let prev_y = y.clone();
        b.iter(|| {
            for i in 0..x.len() {
                swap_xor(&mut x[i], &mut y[i]);
            }
        });
        assert!(prev_x == y);
        assert!(prev_y == x);
    }

    #[bench]
    fn bench_swap_temp(b: &mut Bencher) {
        let (mut x, mut y) = gen_vecs();
        let prev_x = x.clone();
        let prev_y = y.clone();
        b.iter(|| {
            for i in 0..x.len() {
                swap_temp(&mut x[i], &mut y[i]);
            }
        });
        assert!(prev_x == y);
        assert!(prev_y == x);
    }

    #[bench]
    fn bench_swap_std(b: &mut Bencher) {
        let (mut x, mut y) = gen_vecs();
        let prev_x = x.clone();
        let prev_y = y.clone();
        b.iter(|| {
            for i in 0..x.len() {
                swap_std(&mut x[i], &mut y[i]);
            }
        });
        assert!(prev_x == y);
        assert!(prev_y == x);
    }
}
