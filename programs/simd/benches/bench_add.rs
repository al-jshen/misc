use compute::distributions::*;
use criterion::{criterion_group, criterion_main, Criterion};
use rayon::prelude::*;
use std::arch::x86_64::*;

fn add_normal(a: &[f64], b: &[f64]) -> Vec<f64> {
    assert_eq!(a.len(), b.len());
    a.iter().zip(b).map(|(i, j)| i + j).collect()
}

fn add_normal_par(a: &[f64], b: &[f64]) -> Vec<f64> {
    assert_eq!(a.len(), b.len());
    a.par_iter().zip(b).map(|(i, j)| i + j).collect()
}

unsafe fn add_simd(a: &[f64], b: &[f64]) -> Vec<f64> {
    assert_eq!(a.len(), b.len());
    let mut c = Vec::with_capacity(a.len());
    (a.chunks_exact(4).zip(b.chunks_exact(4)))
        .enumerate()
        .for_each(|(idx, (i, j))| {
            let a_pd = _mm256_loadu_pd(i.as_ptr());
            let b_pd = _mm256_loadu_pd(j.as_ptr());
            let c_pd = _mm256_add_pd(a_pd, b_pd);
            _mm256_storeu_pd(
                (c.as_mut_ptr() as *mut f64).offset((idx * 4) as isize),
                c_pd,
            );
            // let a_pd = _mm256_loadu_pd(i.as_ptr().offset(4));
            // let b_pd = _mm256_loadu_pd(j.as_ptr().offset(4));
            // let c_pd = _mm256_add_pd(a_pd, b_pd);
            // _mm256_storeu_pd(
            //     (c.as_mut_ptr() as *mut f64).offset((idx * 4 + 4) as isize),
            //     c_pd,
            // );
        });
    c.set_len(a.len());
    c
}

unsafe fn add_simd_par(a: &[f64], b: &[f64]) -> Vec<f64> {
    assert_eq!(a.len(), b.len());
    // let mut c = Vec::with_capacity(a.len());
    a.par_chunks_exact(4)
        .zip(b.par_chunks_exact(4))
        .map(|(i, j)| {
            let a_pd = unsafe { _mm256_loadu_pd(&i[0]) };
            let b_pd = unsafe { _mm256_loadu_pd(&j[0]) };
            let c_pd = unsafe { _mm256_add_pd(a_pd, b_pd) };
            std::mem::transmute(c_pd)
        })
        .collect::<Vec<[f64; 4]>>()
        .into_iter()
        .flatten()
        .collect::<Vec<f64>>()
}

fn criterion_benchmark(c: &mut Criterion) {
    let n = Normal::default();
    let x = n.sample_n(1000000);
    let y = n.sample_n(1000000);
    c.bench_function("normal add 1e6", |b| {
        b.iter(|| add_normal(&x, &y));
    });
    // c.bench_function("par normal add 1e6", |b| {
    //     b.iter(|| add_normal_par(&x, &y));
    // });
    c.bench_function("simd add 1e6", |b| {
        b.iter(|| unsafe { add_simd(&x, &y) });
    });
    // c.bench_function("par simd add 1e6", |b| {
    //     b.iter(|| unsafe { add_simd_par(&x, &y) });
    // });
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
