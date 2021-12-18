#include <stdio.h>

void add(double *a, double *b, double *c, size_t n) {
  for (int i = 0; i < n; i++) {
    c[i] = a[i] + b[i];
  }
}

int main() {

  double a[10], b[10], c[10];
  for (int i = 0; i < 10; i++) {
    a[i] = i;
    b[i] = i;
  }

  add(a, b, c, 11);

  for (int i = 0; i < 10; i++) {
    printf("%f\n", c[i]);
  }
}
