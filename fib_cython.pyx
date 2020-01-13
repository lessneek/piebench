# cython: language_level=3

cpdef double fib_naive(double n):
    if n <= 2:
        return 1
    else:
        return fib_naive(n - 1) + fib_naive(n - 2)

cpdef int fib_naive_tail(int n, int a=0, int b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return fib_naive_tail(n - 1, b, a + b)
