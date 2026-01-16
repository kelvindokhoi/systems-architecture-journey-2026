# Packages and Modules in Go

### 1. What is a Package?

Every Go program is made up of packages.

Usually we put `package main` at the top of the main program file to indicate that this is the entry point at the `main()` function.
A package named `main` will be compiled into an executable program.

A package by any other name is a `library package`. Libraries have no entry point.
Libraries simply export functionalities that can be used by other packages. For example:

```go
package main

import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("My favorite number is", rand.Intn(10))
}
```

This program is an executable. It is a `main` package and imports from the `fmt` and `math/rand` library packages.

### 2. Package naming
By convention, a package's name is the same as the last element of its import path. For instance, the package imported with the path `math/rand` is named `rand`.

When you create your own packages, it's a good practice to follow this convention to avoid confusion.

That said, package names aren't required to match their import path.

For example, you could have a package with the path `github.com/username/myutils` but name the package `utils`:

```go
package utils
```

### 3. One package per directory
A directory of Go code can have at most one package. All `.go` files in a single directory must all belong to the same package. If they don't, an error will be thrown by the compiler. This is true for main and library packages alike.

### 4. Modules

Go programs are organized into **packages**. A package is a directory in Go code that's all compiled together. Functions, types, vars, and consts defined in one source file are all visible to all other source files **within the same package (directory)**.

A repository contains one or more **modules**. A module is a collection of Go packages that are released together.

![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/IyRpjCm-1280x544.png)

### 5. One module per repository

A file named `go.mod` at the root of a project declares the module. It contains:
- The module path
- The version of the Go language your project requires
- Optionally, any external package dependencies your project has

The module path is just the import path prefix for all packages within the module. Here's an example of a go.mod file:

```go
module github.com/bootdotdev/exampleproject

go 1.25.1

require github.com/google/examplepackage v1.3.0
```

Each module's path not only serves as an import path prefix for the packages within but also indicates where the go command should look to download it. For example, to download the module `golang.org/x/tools`, the go command would consult the repository located at [https://golang.org/x/tools](https://golang.org/x/tools).

An "import path" is a string used to import a package. A package's import path is its module path joined with its subdirectory within the module. For example, the module `github.com/google/go-cmp` contains a package in the directory `cmp/`. That package's import path is `github.com/google/go-cmp/cmp`. Packages in the standard library do not have a module path prefix.
