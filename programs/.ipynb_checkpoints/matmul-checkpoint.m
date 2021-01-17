N = 4096;
A = single(rand(N, N));
B = single(rand(N, N));
start = clock();
C = A * B;
elapsedTime = etime(clock(), start);
gFlops = 2 * N * N * N / (elapsedTime * 1e9);
disp (gFlops)
