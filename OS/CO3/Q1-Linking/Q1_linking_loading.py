"""
Q1 - Linking, Loading and Address Binding
Python demonstration of on-demand library loading using ctypes.
This is a conceptual companion to the assignment's C dlopen()/dlsym() task.
"""
import ctypes
import ctypes.util
import os
import sys

print("Python executable:", sys.executable)
print("Process ID:", os.getpid())
print("Address binding demonstration:")
print("- Compile-time binding: addresses fixed by compiler/linker where applicable.")
print("- Load-time binding: loader resolves relocations when program starts.")
print("- Run-time binding: a library/symbol is selected while the program is running.")

library_name = ctypes.util.find_library("m")
if not library_name:
    print("Math shared library was not found on this system.")
    raise SystemExit(0)

try:
    math_lib = ctypes.CDLL(library_name)
    cos_fn = math_lib.cos
    cos_fn.argtypes = [ctypes.c_double]
    cos_fn.restype = ctypes.c_double
    print(f"Loaded library at run time: {library_name}")
    print("cos(0.0) =", cos_fn(0.0))
except OSError as exc:
    print("Could not load shared library:", exc)

print("\nLinux-only inspection commands:")
print("  ldd ./dynamic_program")
print("  cat /proc/<PID>/maps")
print("Compare executable sizes with: ls -lh static_program dynamic_program")
