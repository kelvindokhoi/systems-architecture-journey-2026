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


### 6. Import Paths
An "import path" is a string used to import a package. A package's import path is its module path joined with its subdirectory within the module. For example, the module `github.com/google/go-cmp` contains a package in the directory `cmp/`. That package's import path is `github.com/google/go-cmp/cmp`. Packages in the standard library do not have a module path prefix.

### 7. Directory Structure

- We will have many git repo on our machine. Typically one per project.
- Each repo is typically one module. The root of the repo contains the `go.mod` file.
- Each modules contains one or more packages. Each package is a directory with `.go` files.
- Each package contains one or more `.go` files in a single directory.

The path to a package's directory determines its import path and where it can be downloaded from if we decide to host it on a remote cersion control system like GitHub or GitLab.

### 8. $GOPATH

The `$GOPATH` env variable is set by default somewhere, typically, `~/go`. We should avoid working in the `$GOPATH/src` directory directly. That's the old way of doing things and may cause unexpected issues.

### 9. Go Install

The go install command compiles and installs a package or packages on your local machine for your personal usage. It installs the package's compiled binary in the GOBIN directory. (We installed the bootdev cli with it, after all)

First, we make a folder:
```bash
mkdir hellogo
cd hellogo
go mod init {REMOTE}/{USERNAME}/hellogo
```

To include another package, we can modify the `go.mod` file like so (`nano go.mod`):
```bash
module github.com/kelvindokhoi/hellogo

go 1.24.4

replace github.com/kelvindokhoi/mystrings v0.0.0 => ../mystrings
require github.com/kelvindokhoi/mystrings v0.0.0
```

To make your own package installable, ensure that:
- Your package is a `main` package (i.e., it has `package main` at the top of the file)
- It has a `main()` function as the entry point
run:
```go
go build
```

Go to your repo root (where go.mod is) and run:

```bash
go install
```

to install an online package, we use `go get`:

```bash
go get github.com/wagslane/go-tinytime
```

### 10. Clean packages
1. Hide internal logic:
We want to hide functions that aren't meant to be use outside the package.
In Go, functions with names starting with a lowercase letter are unexported.
Functions starting with an uppercase letter are exported.
```go
package mypackage
func ExportedFunction() {
	// This function can be accessed from other packages
}
func unexportedFunction() {
	// This function cannot be accessed from other packages
}
```

2. Don't change API:
The unexported functions can be changed without affecting the users of the package. Often for testing, refactoring, and bug fixing.

A well-deisgned library package will have a stable (consistent) API so that the users don't get breaking changes. In Go, this means keeping the function signatures of exported functions the same across versions.

3. Don't export functions from the main package:

A `main` package is not a library, there's no need to export functions from it.

4. Package should not know about dependents:

Perhaps one of the most important and most broken rules is that a package shouldn't know anything about its dependents. In other words, a package should never have specific knowledge about a particular application that uses it.