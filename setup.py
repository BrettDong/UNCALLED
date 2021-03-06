from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext
from distutils.sysconfig import get_python_inc
import os
import subprocess
import sys

uncalled = Extension(
    "uncalled.mapping",
     sources = [
                "src/uncalled.cpp",
                "src/client_sim.cpp",
                "src/fast5_reader.cpp",
                "src/mapper.cpp",
                "src/self_align_ref.cpp",
                "src/map_pool.cpp",
                "src/event_detector.cpp", 
                "src/read_buffer.cpp",
                "src/chunk.cpp",
                "src/realtime_pool.cpp",
                "src/seed_tracker.cpp", 
                "src/normalizer.cpp", 
                "src/range.cpp",
                "src/bwa/bntseq.c",
                "src/bwa/bwt.c",
                "src/bwa/utils.c"],
     include_dirs = ["./",
                     "./pybind11/include", 
                     "./fast5/include",
                     "./pdqsort",
                     "./toml11"],
     libraries = ["hdf5", "z", "dl", "m"],
     extra_compile_args = ["-std=c++11", "-O3", "-march=native", "-mtune=native"],
     define_macros = [("PYBIND", None)]
)

setup(name = "uncalled",
      version = "1.3",
      description = "Rapidly maps raw nanopore signal to DNA references",
      author = "Sam Kovaka",
      author_email = "skovaka@gmail.com",
      url = "https://github.com/skovaka/UNCALLED",
      packages=['uncalled'],
      package_dir = {'': 'src', 'uncalled': 'src/uncalled'},
      py_modules = ['uncalled.params', 'uncalled.minknow_client', 'uncalled.index', 'uncalled.pafstats'],
      ext_modules = [uncalled],
      package_data = {'uncalled': ['models/*', 'conf/*']},
      scripts = ['scripts/uncalled'])
