fn main() {
    let n = 5;
    let rounds = 10;
    let mut scores = vec![0.; n];
    let mut bowls = vec![0.; n];
    bowls[0] = f32::INFINITY;

    let mut r = roll();
    for _ in 0..rounds {
        println!("--------------- {:?}", scores);
        for i in 0..(n - 2) {
            r = roll();
            let mut shift = if i > 0 { f32::min(bowls[i], r) } else { r };
            bowls[i + 1] += shift;
            bowls[i] -= shift;
            scores[i] += shift - 3.5;
            println!("{:?} {}", bowls, shift);
        }
        r = roll();
        let mut shift = f32::min(bowls[n - 1], r);
        bowls[n - 1] -= shift;
        scores[n - 1] += shift - 3.5;
        println!("{:?} {}", bowls, shift);
    }
}

fn roll() -> f32 {
    fastrand::u64(1..=6) as f32
}
