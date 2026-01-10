# Functions in Go

## 📌 Overview
Functions in Go can take zero or more arguments.

To make code easier to read, the variable type comes after the variable name.

Example:
```go
func sub(x int, y int) int {
    return x-y
}
```

If multiple consecutive parameters share the same type, you can omit the type from all but the last.

Example:
```go
func add(x, y int) int {
    return x + y
}
```

### 1. Go-style Syntax
```go
x int
p *int // pointer to an int
a [3]int // array of 3 ints
s []int // slice of ints. A slice is a dynamically-sized array
m map[string]int // map with string keys and int values
```

It's nice for more complex function signatures:
```go
f func(func(int,int) int, int) int
g map[string]func(int) int
```

### 2. Passing Arguments by Value
In Go, most types are passed by value. Some exceptions are slices, maps, channels, interfaces, and function types, which are reference types.

### 3. Ignoring Return Values
If a function returns multiple values and you want to ignore some of them, use the blank identifier `_`.
Example:
```go
func getPoint() (x int, y int) {
    return 3, 4
}

// ignore y value
x, _ := getPoint()
```

### 4. Named Return Values
You can name the return values in the function signature. This allows you to use a `return` statement without arguments to return the current values of the named return variables.
Example:
```go
func getCoords() (x, y int) {
	// x and y are initialized with zero values

	return // automatically returns x and y
}
```
Which is equivalent to this sniplet while having better readability:
```go
func getCoords() (int, int) {
	var x int
	var y int
	return x, y
}
```
Explicit return statements can be used like in Python.

### 5. Defer Statement
The `defer` statement is used to ensure that a function call is performed later in a program's execution, usually for purposes of cleanup. `defer` is often used with functions that need to release resources, such as closing a file or network connection.
Example:
```go
func GetUsername(dstName, srcName string) (username string, err error) {
	// Open a connection to a database
	conn, _ := db.Open(srcName)

	// Close the connection *anywhere* the GetUsername function returns
	defer conn.Close()

	username, err = db.FetchUser()
	if err != nil {
		// The defer statement is auto-executed if we return here
		return "", err
	}

	// The defer statement is auto-executed if we return here
	return username, nil
}
```

### 6. Block Scope
Unlike Python, Go is not function-scoped but block-scoped. A block is defined by curly braces `{}`.

### 7. Closures
Go supports closures, which are functions that reference variables from outside their own scope.
Example:
```go
package main

func adder() func(int) int {
	var sum int = 0
	return func(number int) (int){
		sum += number
		return sum
	}
}
```

In this example, the inner function returned by `adder` captures the `sum` variable from its enclosing scope. Each time the returned function is called, it updates and returns the cumulative sum.

### 8. Currying
Currying is a techinique to transform a function that takes multiple arguments into a sequence of functions that each take a single argument.
Example:
```go
func multiply(x int) func(int) int {
    return func(y int) int {
        return x * y
    }
}
```