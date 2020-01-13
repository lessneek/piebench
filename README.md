## Performance benchmarks of various python module integrations.

### Compiling of modules

Add `./build/lib.linux-x86_64-3.8/` directory to `PYTHONPATH` (python modules search path). All modules (`*.cpython-38-x86_64-linux-gnu.so`) should be compiled there. Run: `export PYTHONPATH=$PYTHONPATH:./build/lib.linux-x86_64-3.8/`

##### Building the `nim` module:
1. `nimble install nimpy`
2. `nim c -d:release --app:lib --gc:regions --out:./build/lib.linux-x86_64-3.8/fib_nimpy.cpython-38-x86_64-linux-gnu.so fib_nimpy.nim`

##### Building the `cython` module:
1. `pip install Cython`
2. `python setup.py build_ext`

##### Installing dependencies for LUA:
`pip install lupa`

### Exemple of running:
```
fib(42)=267914296 in 47.805s (python)
fib(42)=267914296 in 25.202s (lua)
fib(42)=267914296.0 in 0.520s (cython)
fib(42)=267914296 in 0.455s (nim)
```
