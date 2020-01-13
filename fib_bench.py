import time
from fib_cython import fib_naive as fib_naive_cython
from fib_nimpy import fib_naive as fib_naive_nim
from lupa import LuaRuntime

lua_fib_naive_code = '''
    function(n)
        local function fib(m)
            if m <= 2 then return 1 end
            return fib(m - 1) + fib(m - 2)
        end
        return fib(n)
    end
'''

lua_fib_naive_tail_code = '''
    function(n)
        local function fib(m, a, b)
            a = a or 0
            b = b or 1
            if m == 0 then return a end
            if m == 1 then return b end
            return fib(m - 1, b, a + b)
        end
        return fib(n)
    end
'''

lua_fib_iterative_code = '''
    function(n)
      a, b = 0, 1

      for i = 1, n do
        a, b = b, a + b
      end
      return a
    end
'''


def bench_fib_python(x: int) -> (int, float):
    def fib(n: int) -> int:
        if n <= 2:
            return 1
        return fib(n - 1) + fib(n - 2)

    start = time.perf_counter()
    res = fib(x)
    elapsed = time.perf_counter() - start
    return res, elapsed


def bench_fib_lua(x: int) -> (int, float):
    lua = LuaRuntime(unpack_returned_tuples=True)
    lua_fib = lua.eval(lua_fib_naive_code)
    start = time.perf_counter()
    res = lua_fib(x)
    elapsed = time.perf_counter() - start
    return res, elapsed


def bench_fib_cython(x: int) -> (int, float):
    start = time.perf_counter()
    res = fib_naive_cython(x)
    elapsed = time.perf_counter() - start
    return res, elapsed


def bench_fib_nim(x: int) -> (int, float):
    start = time.perf_counter()
    res = fib_naive_nim(x)
    elapsed = time.perf_counter() - start
    return res, elapsed


def print_result(name: str, x: int, res: int, elapsed: float):
    print(f"fib({x})={res} in {elapsed:.3f}s ({name})")


if __name__ == "__main__":
    x = 42
    benches = {
        'python': bench_fib_python,
        'lua': bench_fib_lua,
        'cython': bench_fib_cython,
        'nim': bench_fib_nim
    }
    for name, bench in benches.items():
        res, elapsed = bench(x)
        print_result(name, x, res, elapsed)
