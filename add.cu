#include <iostream>
using namespace std;

__global__ void init(int n, float *x, float *y) {
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  for (int i = index; i < n; i += stride) {
    x[i] = 1.0f;
    y[i] = 2.0f;
  }
}

__global__ void add(int n, float *x, float *y)
{
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  for (int i = index; i < n; i+= stride) {
    y[i] = x[i] + y[i];
  }
}

int main()
{
  const int N = 1 << 20;
  float *x, *y;
  cudaMallocManaged(&x, N * sizeof(float));
  cudaMallocManaged(&y, N * sizeof(float));

  /* for (int i = 0; i < N; i++) { */
  /*   x[i] = 1.0f; */
  /*   y[i] = 2.0f; */
  /* } */

  int blockSize = 512;
  int numBlocks = (N + blockSize - 1) / blockSize;
  /* cout << "blockSize" << blockSize << endl; */
  /* cout << "numBlocks" << numBlocks << endl; */
  init<<<numBlocks, blockSize>>>(N, x, y);
  add<<<numBlocks, blockSize>>>(N, x, y);

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
