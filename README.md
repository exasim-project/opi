# OPI - A Package Index for FOAM Projects

OPI is a package index for FOAM projects.
It has the goal to simplify discovery and installation of community based packages.

# Adding your Package

Adding a package to the index is simple.
Fork this repository, and add the package meta data as a json file to pck/<your_package>/<your_package>.json.

An example is given below

{
    "name": "ogl",                             # required
    "repo": "github.com/hpsim/OGL.git",        # required
    "description":"GPU capable linear solver", # A short description to print in CLI max 80 chars
    "type": "lib",                             # optional, possible values: [lib,app] 
    "build":  # required, how to build the package, possible values ["wmake", "cmake", ["list of steps"]]
      ["cmake --preset release", "cmake --build --preset release", "cmake --build --preset release --target install"],
    "version": [">=2304", "<8"],               # optional, required FOAM version possible format examples: [  2304, 8, 0.1.0]  
    "keywords": ["GPU", "linear solver"]       # optional keywords for searching and grouping e.g. turbulence, scheme
}

# Usecases

Based on this package index we can build a package manager that can automatically resolve depencies.

# Limitations
