#include <iostream>
using namespace std;

__global__ void add(int n, float x[], float y[])
{
  int index = threadIdx.x;
  int stride = blockDim.x;
  for (int i = index; i < n; i+= stride) {
    y[i] = x[i] + y[i];
  }
}

int main()
{
  const int N = 1e6;
  float *x, *y;
  cudaMallocManaged(&x, N * sizeof(float));
  cudaMallocManaged(&y, N * sizeof(float));

  for (int i = 0; i < N; i++) {
    x[i] = 1.0f;
    y[i] = 2.0f;
  }

  add<<<1, 1024>>>(N, x, y);

  cudaDeviceSynchronize();

  float maxErr = 0.0f;
  for (int i = 0; i < N; i++) {
    maxErr = max(maxErr, abs(y[i] - 3.0f));
  }
  cout << maxErr << endl;

  cudaFree(x);
  cudaFree(y);

  return 0;
}
