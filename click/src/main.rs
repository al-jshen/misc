use compute::linalg::Vector;
use fantoccini::{ClientBuilder, Locator};
use std::time::{Duration, Instant};
use tokio::time::sleep;

#[tokio::main]
async fn main() -> Result<(), fantoccini::error::CmdError> {
    let cb = ClientBuilder::native();

    let mut c = cb.connect("http://localhost:4444").await.unwrap();

    c.goto("https://humanbenchmark.com/tests/reactiontime/")
        .await
        .unwrap();

    sleep(Duration::from_millis(500)).await;

    c.find(Locator::Css(".view-splash")).await?.click().await?;

    let mut times = Vector::empty();

    loop {
        let start = Instant::now();
        match c.find(Locator::Css(".view-go")).await {
            Ok(obj) => {
                obj.click().await.unwrap();
                break;
            }
            Err(_) => sleep(Duration::from_millis(1)).await,
        }
        let end = start.elapsed();
        times.push(end.as_millis() as f64);
    }

    println!("{} {} {}", times.mean(), times.std(), times.len());
    println!("{:?}", times);

    sleep(Duration::from_secs(2)).await;

    c.close().await
}
