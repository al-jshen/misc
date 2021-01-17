#include <iostream>
using namespace std;

void add(int n, float x[], float y[])
{
  for (int i = 0; i < n; i++) {
    y[i] = x[i] + y[i];
  }
}

int main()
{
  const int N = 1e6;
  float* x = new float[N];
  float* y = new float[N];

  for (int i = 0; i < N; i++) {
    x[i] = 1.0f;
    y[i] = 2.0f;
  }

  add(N, x, y);

  float maxErr = 0.0f;
  for (int i = 0; i < N; i++) {
    maxErr = max(maxErr, abs(y[i] - 3.0f));
  }
  cout << maxErr << endl;

  free(x);
  free(y);

  return 0;
}
