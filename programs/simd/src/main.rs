use compute::distributions::*;
use std::arch::x86_64::*;

fn main() {
    // let n = Normal::default();
    // let a = n.sample_n(8);
    // let b = n.sample_n(8);
    // // println!("{:?}", add_normal(&a, &b));
    // println!("{:?}", add_simd(&a, &b));
    let mut a: Vec<f64> = Vec::with_capacity(10);
    unsafe {
        a.set_len(10);
    }
    println!("{:?}", a);
}

fn add_normal(a: &[f64], b: &[f64]) -> Vec<f64> {
    assert_eq!(a.len(), b.len());
    a.iter().zip(b).map(|(i, j)| i + j).collect()
}

fn add_simd(a: &[f64], b: &[f64]) -> Vec<f64> {
    assert_eq!(a.len(), b.len());
    let mut c = Vec::with_capacity(a.len());
    unsafe {
        c.set_len(a.len());
    }
    (a.chunks(4).zip(b.chunks(4)))
        .enumerate()
        .for_each(|(idx, (i, j))| {
            println!("{:?} {:?}", i, j);
            let a_pd = unsafe { _mm256_loadu_pd(&i[0]) };
            let b_pd = unsafe { _mm256_loadu_pd(&j[0]) };
            let c_pd = unsafe { _mm256_add_pd(a_pd, b_pd) };
            unsafe {
                _mm256_storeu_pd(
                    (c.as_mut_ptr() as *mut f64).offset((idx * 4) as isize),
                    c_pd,
                )
            };
        });
    c
}
