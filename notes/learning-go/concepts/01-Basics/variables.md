# Variables in Go

## 📌 Overview
Go is **statically typed**, meaning variable types are determined at compile time. If you don't assign a value, Go automatically assigns a "Zero Value."

### 1. The `var` Keyword
Best for package-level variables or when you want to declare a variable without an immediate value.
```go
var name string = "Gopher"
var age int             // Initialized to 0
var isReady bool        // Initialized to false
var pi float64 = 3.14
var byteValue byte      // Initialized to 0
```

### 2. Print variables

```go
import "fmt"

fmt.Printf("Name: %s, Age: %d, Ready: %t, Pi: %.2f, ByteValue: %d\n", name, age, isReady, pi, byteValue)
```
Note: `%s` for strings, `%d` for integers and bytes, `%t` for booleans, and `%.2f` for floating-point numbers.
How to memorize format specifiers: "s" for string, "d" for digit, "t" for true/false, and "f" for float.

```go
import "fmt"
fmt.Println("Hello,"name)
```
Print multiple variables like in Python.

### 3. Short Variable Declaration
Used within functions for concise variable declaration and initialization.
```go
name := "Gopher"
```

### 4. Same Line Declaration
You can declare and initialize multiple variables of the same type on a single line.
```go
averageOpenRate, displayMessage := .23, "is the average open rate of your messages"
```

### 5. Type Sizes
Go provides specific types with defined sizes for better control over memory usage.
Signed Integers: `int8`, `int16`, `int32`, `int64`
Unsigned Integers: `uint8`, `uint16`, `uint32`, `uint64`, `uintptr` (note: `uint8` is also known as `byte`, `int32` as `rune` and used for Unicode code points, and `uintptr` is used for pointer arithmetic)
Signed Floating-Point Numbers: `float32`, `float64`
Complex Numbers: `complex64`, `complex128`

The size of the type indicates the number of bits.

Fact: Go is statically typed, so every variable must have a defined type at compile time.

Convert between types using explicit conversion:
```go
temperatureFloat := 88.26
temperatureInt := int64(temperatureFloat) // Converts float64 to int64
```

Default types when not specified:
`bool`
`string`
`int`
`uint`
`byte`
`rune`
`float64`
`complex128`

When should you elect to NOT use a 'default type'?
When performance and memory are the primary concern.

### 6. Concatenate strings

```go
	var username string = "presidentSkroob"
	var password string = "12345"
    fmt.Println("Authorization: Basic", username+":"+password)
```
Two strings can be concatenated with the + operator. But the compiler will not allow you to concatenate a string variable with an int or a float64.

### 7. Constants
Constants are immutable values that cannot be changed after declaration. Use the `const` keyword.
```go
const Pi = 3.14
const TwoPi = Pi * 2 // for calculated constants
```
Note:
We can't declare constants using the short variable declaration syntax (`:=`)
OR
constants that are computed at runtime (e.g., using function calls).
Example:
```go
const currentTime = time.Now() // This will cause a compile-time error
```

### 8. Formatting Strings
You can use the `fmt.Sprintf` function to create formatted strings without printing them directly.
```go
s := fmt.Sprintf("I am %d years old", 10)
```

### Observations
Unlike C, we don't need to use semicolons (`;`) at the end of each statement in Go. The Go compiler automatically inserts them where necessary.
To format strings, %v can be used as a general placeholder for any type.