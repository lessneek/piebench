import nimpy

proc fib_naive(n: int): int {.exportpy.} =
  if n <= 2:
    return 1
  return fib_naive(n - 1) + fib_naive(n - 2)

proc fib_iterative(n: int): int {.exportpy.} =
  var a, b: int
  a = 0
  b = 1

  for i in 1..n:
    (a, b) = (b, a + b)

  return a

proc fib_naive_tail(n: int, a: int = 0, b: int = 1): int {.exportpy.} =
  if n == 0:
    return a
  if n == 1:
    return b
  return fib_naive_tail(n - 1, b, a + b)
